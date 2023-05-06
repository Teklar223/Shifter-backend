from ortools.sat.python import cp_model
from base_app.mongo.SchedulingAlgorithm.PreProcessing import preprocessing
from copy import deepcopy
from base_app.mongo.SchedulingAlgorithm.Tuple_Key import Tuple_Key
from base_app.mongo.SchedulingAlgorithm.Utils import get_maximal_workers_dict, get_shift_str
from base_app.mongo.Models.PostAssignment.AssignedWeek import AssignedDay, AssignedEvent, AssignedWeek
import json
from base_app.mongo.Models import Schedule, Shift



# TODO: update maximum hours per day
# Assuming that I get a dictionary from employee_id to role_id, seperate by roles and run the algorithm seperately



def schedule(shift_id, employee_roles):

    """
    get the needed data for the algorithm using the preprocessing function
    """

    schedule_template, preferences_template, roles, sc = preprocessing(shift_id=shift_id, employees_roles=employee_roles)
    week = AssignedWeek(shift_id=shift_id, start_date=sc.get_start_date(), end_date=sc.get_end_date(),
                         company_id=sc.get_company_id(), team_id=sc.get_team_id())
    

    """
    Create the basic object of a week using the schedule object and add empty days to it
    """

    
    for daily in sc.get_daily_shifts():
        date = daily.get_date()
        start_hour = daily.get_start_hour()
        end_hour = daily.get_end_hour()
        week += AssignedDay(date=date, start_hour=start_hour, end_hour=end_hour)

    """
    add the events to the days
    """

    for role in roles:
        output = run(schedule_template=schedule_template.get(role), preferences_template_list=preferences_template.get(role))
        for date, events in output.items():
            for event in events:
                week.add_event(date, event)
    
    return week


def run(schedule_template, preferences_template_list):
    employees = [x.get("EmployeeID") for x in preferences_template_list] # list of employee ids
    dates = [x for x in schedule_template.keys()]
    shifts = {}
    model = cp_model.CpModel()
    keys = []
    maximal_dict = get_maximal_workers_dict(shift_template=schedule_template)

    """
    Create the basic model, assign boolean variable to each (employee, date, shift) object
    """

    for template in preferences_template_list:
        employee_id = template.get("EmployeeID")
        for daily in template.get("Dailies"):
            date = daily.get("Date")
            for shift in daily.get("ShiftTypes"):
                shift_copy, shift_str = get_shift_str(shift, "Answer")
                key = Tuple_Key(employee_id=employee_id, date=date, shift=shift_copy)
                shifts[key] = model.NewBoolVar('shift_%s' % (shift_str))
                keys.append(key)

    """
    Limit each shift with the maximal number of worker that defined for it
    """

    for date, shifts2 in schedule_template.items():
        for shift in shifts2:
            shift_copy, shift_str = get_shift_str(shift=shift, item="Workers")
            employees_for_shift = [x.get_employee_id() for x in list(filter(lambda obj: obj.get_date() == date and obj.get_shift() == shift_str, keys))]
            if len(employees_for_shift) == 0:
                continue
            maximal = maximal_dict.get(date).get(shift_str)
            model.Add(sum(shifts[Tuple_Key(employee_id=e_id, date=date, shift=shift_copy)] for e_id in employees_for_shift) <= maximal)
    
    # """
    # prepare to finalize:
    # """

    # for x in shifts:
    #     print(x)


    model.Maximize(sum(shifts[key] for key in keys))

    solver = cp_model.CpSolver()
    status = solver.Solve(model)
    days = dict()

    # collect the data and return the result

    if status == cp_model.OPTIMAL:
        for key in keys:
            if solver.Value(shifts[key]) == 1:
                date = key.get_date()
                if days.get(date) is None:
                    days[date] = []
                employee_id = key.get_employee_id()
                data = key.get_data()
                start_hour = data["StartHour"]
                end_hour = data["EndHour"]
                event = AssignedEvent(employee_id=employee_id, start_hour=start_hour, end_hour=end_hour)
                days.get(date).append(event)
    return days


