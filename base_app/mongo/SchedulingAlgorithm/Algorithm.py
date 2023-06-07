from ortools.sat.python import cp_model
from base_app.mongo.SchedulingAlgorithm.PreProcessing import preprocessing
from copy import deepcopy
from base_app.mongo.SchedulingAlgorithm.Tuple_Key import Tuple_Key
from base_app.mongo.SchedulingAlgorithm.Utils import get_maximal_workers_dict, get_shift_str
from base_app.mongo.Models.PostAssignment.AssignedWeek import AssignedDay, AssignedEvent, AssignedWeek
import json
from base_app.mongo.Models import Schedule, Shift
from base_app.mongo.SchedulingAlgorithm.Strategies.Stratrgy import Strategy
<<<<<<< HEAD
from base_app.mongo.SchedulingAlgorithm.Strategies.HourStrategies.MaxHoursStrategy import Max_Hour_Daily_Strategy
from base_app.mongo.SchedulingAlgorithm.Strategies.HourStrategies.MaxHoursSchedule import Max_Hour_Schedule_Strategy
from base_app.mongo.SchedulingAlgorithm.Strategies.StrategyUtils import get_strategies, divide_strategies_by_role, isIntersect
=======
from .Strategies.HourStrategies.MaxHoursStrategy import Max_Hour_Daily_Strategy
from .Strategies.HourStrategies.MaxHoursSchedule import Max_Hour_Schedule_Strategy
from .Strategies.StrategyUtils import get_strategies, divide_strategies_by_role, isIntersect

>>>>>>> 52e50f378f239d3dbc718fbca6d1a4a86f81f304

# TODO: update maximum hours per day
# Assuming that I get a dictionary from employee_id to role_id, seperate by roles and run the algorithm seperately


def schedule(shift_id, employee_roles, strategies):

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

    roles_strategies, global_strategies = divide_strategies_by_role(strategies_dict=strategies,
                                                                    roles=roles,
                                                                    employees_roles=employee_roles)
    for role in roles:
        role_strategies = roles_strategies.get(role)
        if role_strategies is None:
            role_strategies = dict()
        output = run(schedule_template=schedule_template.get(role),
                      preferences_template_list=preferences_template.get(role),
                      role_strategies=role_strategies, global_strategies=global_strategies)
        for date, events in output.items():
            for event in events:
                week.add_event(date, event)
    
    return week


def run(schedule_template, preferences_template_list, role_strategies, global_strategies):
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
            daily_keys = []
            for shift in daily.get("ShiftTypes"):
                shift_copy, shift_str = get_shift_str(shift, "Answer")
                answer = shift.get("Answer")
                key = Tuple_Key(employee_id=employee_id, date=date, shift=shift_copy)
<<<<<<< HEAD
                shifts[key] = model.NewBoolVar('shift_%s' % (shift_str))
                keys.append(key)
            employee_daily_keys = [x for x in list(filter(lambda obj: obj.get_date() == date and obj.get_employee_id() == employee_id, keys))]
            
            """
            Use a constraint to prevent overlapping of shifts
            S1 = (a, b)
            S2 = (c,d)
            overlapping = (a<c<b) or (a<d<b) or (c<a<d) or (c<b<d)
            in that case we would like to allow only one shift at most to be assigned.
            x1 the assignment of S1
            X2 the assignment of S2
            x1 + x2 <= 1
            """
            
            for i in range(len(employee_daily_keys) - 1):
                key_i = employee_daily_keys[i]
                for j in range(i + 1, len(employee_daily_keys)):
                    key_j = employee_daily_keys[j]
                    if isIntersect(key_i, key_j):
                        model.Add(shifts.get(key_i) + shifts.get(key_j) <= 1)
=======
                if answer is True:
                    shifts[key] = model.NewBoolVar('shift_%s' % (shift_str))
                    keys.append(key)
                    daily_keys.append(key)

            """
            Prevent overlapping of shifts
            """

            for i in range(len(daily_keys) -1):
                for j in range(i+1, len(daily_keys)):
                    key_i = daily_keys[i]
                    key_j = daily_keys[j]
                    if isIntersect(key1=key_i, key2=key_j):
                        model.Add(shifts.get(key_i) + shifts.get(key_j) <= 1)

            
>>>>>>> 52e50f378f239d3dbc718fbca6d1a4a86f81f304

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

    """
    Create a list of strategies and execute them
    """

    role_strategies_list = get_strategies(strategies_dict=role_strategies, shift_keys=keys)
    global_strategies_list = get_strategies(strategies_dict=global_strategies, shift_keys=keys)
    strategies_list = role_strategies_list + global_strategies_list
    for strategy in strategies_list:
        model = strategy.execute(model=model, shifts=shifts)
    


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


