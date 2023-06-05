from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from ..mongo.Shifts_Handler import Shifts_Handler, Shift, Schedule # Handler and models
from ..mongo.WeeklyPref_Handler import WeeklyPrefHandler, DailyPref, WeeklyPref # Handler and models
# from ..mongo.AssignmentsHandler import AssignmentsHandler
from ..mongo.constants import *
from ..constants import team_id, company_id, employee_id
from ..mongo.constants import Shift_id, Employee_id, Team_id, Company_id, INPUT_SIGNATURE
from ..mongo.Models.PostAssignment.AssignedWeek import AssignedWeek, AssignedEvent, AssignedDay
from ..mongo.AssignmentsHandler import Assignment_Handler
from ..mongo.SchedulingAlgorithm.Algorithm import schedule
''' Shifts  '''

def ShiftsGet(request, *args, **kwargs) -> JsonResponse:
    ''''
        @ team_id is passed throguh kwargs (as a slug)
        @ shift_id is passed in *BODY*
    '''
    # TODO: pass a list of team id's in the body instead of through the slug and retrieve their shifts
    # TODO: sort by date (for example last n weeks and m next weeks)
    if team_id in kwargs:
        handler: Shifts_Handler = Shifts_Handler()
        shifts = handler.get_recent_shifts_by_team_id(team_id = kwargs.get(team_id))
        json_shifts = [x.get_dict_format() for x in shifts]
        return JsonResponse(json_shifts, safe=False)
    else:
        data = JSONParser().parse(request)
        if Shift_id in data:
            handler : Shifts_Handler = Shifts_Handler()
            schedule : Schedule = handler.get_schedule_by_shift_id(shift_id=data.get(Shift_id))
            return JsonResponse(schedule.get_dict_format(), safe=False)
        else:
            return JsonResponse("No team_id for ShiftsGet :(", safe=False)
    
"""
case 1:
Create new shift
format example: 
{
    'CompanyID': 9,
    'TeamID': 7,
    'StartDate': 9, 
    'EndDate': 67, 
    'DailyShifts': 
        [
            {
                'Date': 1, 
                'StartHour': 1, 
                'EndHour': 1, 
                'PossibleShifts': 
                    [
                        {
                            'ShiftName': 'Evening',
                            'StartHour': 1900, 
                            'EndHour': 2330, 
                            'NeededRoles': 
                                [
                                    {
                                        'RoleID': 1500, 
                                        'NeededWorkers': 54
                                    }, 
                                    {
                                        'RoleID': 1510, 
                                        'NeededWorkers': 12
                                    }
                                ]
                        },
                        {
                            'ShiftName': 'Morning', 
                            'StartHour': 800, 
                            'EndHour': 1800, 
                            'NeededRoles': 
                                [
                                    {
                                        'RoleID': 1500, 
                                        'NeededWorkers': 5
                                    }
                                ]
                        }
                    ]
                }, 
                {
                    'Date': 2, 
                    'StartHour': 1, 
                    'EndHour': 1, 
                    'PossibleShifts': 
                        [
                            {
                                'ShiftName': 'Morning', 
                                'StartHour': 1700, 
                                'EndHour': 2200, 
                                'NeededRoles': 
                                    [
                                        {
                                            'RoleID': 1500, 
                                            'NeededWorkers': 3
                                        }
                                    ]
                            }
                        ]
                }
        ],
        'ShiftID': '643db236077a1bb573e4339a'
}
"""

def ShiftsPost(request, *args, **kwargs) -> JsonResponse:
    if company_id in kwargs and team_id in kwargs:
        handler: Shifts_Handler = Shifts_Handler()
        data = JSONParser().parse(request)
        schedule = handler.get_schedule_from_doc(data)
        handler.add_new_shift(schedule = schedule)
        return JsonResponse(status=201)
    else:
        pass

def ShiftsPut(request, *args, **kwargs) -> JsonResponse:
    handler: Shifts_Handler = Shifts_Handler()
    pass

def ShiftsDelete(request, *args, **kwargs) -> JsonResponse:
    handler: Shifts_Handler = Shifts_Handler()
    pass

''' WeeklyPref  '''

"""
case 1:
get the preferences of specific employee
format:
{
    "EmployeeID": ...
}

case 2:
get the preferences of specific team
format:
{
    "TeamID": ...
}
"""

def WeeklyPrefGet(request, *args, **kwargs) -> JsonResponse: # need to check
    if employee_id in kwargs:
        handler : WeeklyPrefHandler = WeeklyPrefHandler()
        data = handler.get_employee_preferences(kwargs.get(employee_id))
        if len(data) == 1: # will be 1 or 0
            return JsonResponse(data[0].get_dict_format(), safe=False, status=201)
        else:
            pass
    elif team_id in kwargs:
        handler : WeeklyPrefHandler = WeeklyPrefHandler()
        data = handler.get_team_preferences(team_id=kwargs.get(team_id))
        data_dict = [d.get_dict_format() for d in data]
        return JsonResponse(data_dict, safe=False, status=201)
    else:
        pass

"""
case 1:
the input json is a employee id and schedule, and we need to derive it to weekly preferences 
format:
{
    "EmployeeID": ...,
    "Schedule": ...The dictionary representation of Schedule object
}
the schedule should be the schedule of the next week.
"""

def WeeklyPrefPost(request, *args, **kwargs) -> JsonResponse:
    data = JSONParser().parse(request)
    if employee_id in kwargs:
        shift_handler : Shifts_Handler = Shifts_Handler()
        schedule = shift_handler.get_schedule_from_doc(data)
        e_id = kwargs.get(employee_id)
        handler : WeeklyPrefHandler = WeeklyPrefHandler()
        wp = handler.derive_preferences_from_schedule(employee_id=e_id, schedule=schedule, default_pref=False)
        handler.add_first_pref(wp=wp)
        return JsonResponse(data=wp.get_dict_format(), safe=False, status=201)

    # if Employee_id in kwargs and Team_id in kwargs:
    #     handler = WeeklyPrefHandler()
    #     handler.add_first_pref(wp=handler.get_wp_from_doc(doc=kwargs))
    else:
        pass
        
        """
        case 1:
        This function will work if there is at least one document in Shifts and document for each
        employee in WeeklyPref collection
        format:
        {
            "TeamID": ...
        }

        case 2:
        This function will update the preferences of an employee
        format:
        {
            "EmployeeID": ...,
            "Preferences": ...The dictionary representation of WeeklyPref object
        }
        """

def WeeklyPrefPut(request, *args, **kwargs) -> JsonResponse:
    if team_id in kwargs:
        t_id = kwargs.get(team_id)
        shift_handler : Shifts_Handler = Shifts_Handler()
        data = JSONParser().parse(request)
        schedule : shift_handler.get_schedule_from_doc(data)
        handler : WeeklyPrefHandler = WeeklyPrefHandler()
        wp_list = handler.get_team_preferences()
        e_id = -1
        if len(wp_list) > 0:
            wp = wp_list[0]
            e_id = wp.get_employee_id()
            new_wp = handler.derive_preferences_from_schedule(employee_id=e_id, schedule=schedule)
            handler.prepare_team_next_weekly_pref(team_id=t_id, wp=new_wp)
            return JsonResponse(status=201)
    elif employee_id in kwargs:
        e_id = kwargs.get(employee_id)
        handler : WeeklyPrefHandler = WeeklyPrefHandler()
        data = JSONParser().parse(request)
        wp : WeeklyPref = handler.get_wp_from_doc(data)
        handler.update_employee_next_weekly_pref(employee_id=e_id, wp=wp)
        return JsonResponse(status=201)



def WeeklyPrefDelete(request, *args, **kwargs) -> JsonResponse:
    pass

''' Assignments  '''

"""
case 1: get assignment by ShiftID
case 2: get assignment by date
case 3: get assignment by team(recent assignments)
"""

def AssignmentsGet(request, *args, **kwargs) -> JsonResponse:
    if Shift_id in kwargs:
        handler : Assignment_Handler = Assignment_Handler()
        assignment : AssignedWeek = handler.get_assignment_by_shift_id(kwargs.get(Shift_id))
        return JsonResponse(data=assignment.get_dict_format(), safe=False)
        # TODO: merge with the algorithm branch to continue
    elif date in kwargs:
        pass # TODO: implement the function first
    elif team_id in kwargs:
        t_id = kwargs.get(team_id)
        handler : Assignment_Handler = Assignment_Handler()
        if "count" in kwargs:
            count = kwargs.get("count")
            if isinstance(count, int) and count > 0:
                data = handler.get_recent_assignments_by_team_id(team_id=t_id, count=count)
            else:
                data = handler.get_recent_assignments_by_team_id(team_id=t_id)
            data_dict = [d.get_dict_format() for d in data]
            return JsonResponse(data=data_dict, safe=False)
        else:
            data = handler.get_recent_assignments_by_team_id(team_id=t_id)
            data_dict = [d.get_dict_format() for d in data]
            return JsonResponse(data=data_dict, safe=False)


def AssignmentsPost(request, *args, **kwargs) -> JsonResponse:
    data = JSONParser().parse(request)
    handler : Assignment_Handler = Assignment_Handler()
    assignment = AssignedWeek.dict_to_week_obj(data)
    handler.add_new_assignment(assignment=assignment)
    return JsonResponse(safe=False, status=201)

def AssignmentsPut(request, *args, **kwargs) -> JsonResponse:
    data = JSONParser().parse(request)
    handler : Assignment_Handler = Assignment_Handler()
    assignment = AssignedWeek.dict_to_week_obj(data)
    handler.update_assignment(assignment=assignment)
    return JsonResponse(safe=False, status=201)

def AssignmentsDelete(request, *args, **kwargs) -> JsonResponse:
    pass

"""
Needed inputs in kwargs: ShiftID
Needed input in body: {"Strategy Inputs": {inputs dictionary of dictionaries}}
"""

def SchedulingAlgorithmRun(request, *args, **kwargs) -> JsonResponse:
    if Shift_id in kwargs:
        s_id = kwargs.get(Shift_id)
        shift_handler : Shifts_Handler = Shifts_Handler()
        schedule = shift_handler.get_schedule_by_shift_id(shift_id=s_id)
        t_id = schedule.get_team_id()
        team_data = None # TODO: after merge get the data of the team and save it in this variable
        employees_roles = dict()
        for entry in team_data:
            employee_id = entry.email
            role_id = entry.role_id
            employees_roles[employee_id] = role_id
        input_condition = None
        data = JSONParser().parse(request)
        if INPUT_SIGNATURE in data:
            input_condition = data.get(INPUT_SIGNATURE)
        output : AssignedWeek = schedule(Shift_id=s_id, employee_roles=employees_roles, strategies=input_condition)
        output_data = output.get_dict_format()
        return JsonResponse(data=output_data, safe=False)