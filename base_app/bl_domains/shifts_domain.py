from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from ..mongo.Shifts_Handler import Shifts_Handler, Shift, Schedule # Handler and models
from ..mongo.WeeklyPref_Handler import WeeklyPrefHandler, DailyPref, WeeklyPref # Handler and models
# from ..mongo.AssignmentsHandler import AssignmentsHandler
from ..mongo.constants import *
from ..constants import team_id, company_id

''' Shifts  '''

def ShiftsGet(request, *args, **kwargs) -> JsonResponse:
    if team_id in kwargs:
        handler: Shifts_Handler = Shifts_Handler()
        shifts = handler.get_recent_shifts_by_team_id(team_id = team_id)
        return JsonResponse(shifts.data, safe=False)
    else:
        return JsonResponse("No team_id for ShiftsGet :(", safe=False)

def ShiftsPost(request, *args, **kwargs) -> JsonResponse:
    if company_id in kwargs and team_id in kwargs:
        handler: Shifts_Handler = Shifts_Handler()
        data = JSONParser().parse(request)
        c_id = kwargs.get(company_id)
        t_id = kwargs.get(team_id)
        s_date = data.get(Start_date)
        e_date = data.get(End_date)
        schedule = Schedule(company_id = c_id, team_id = t_id, startdate = s_date, enddate= e_date)
        handler.add_new_shift(schedule = schedule)
    else:
        pass

def ShiftsPut(request, *args, **kwargs) -> JsonResponse:
    handler: Shifts_Handler = Shifts_Handler()
    pass

def ShiftsDelete(request, *args, **kwargs) -> JsonResponse:
    handler: Shifts_Handler = Shifts_Handler()
    pass

''' WeeklyPref  '''

def WeeklyPrefGet(request, *args, **kwargs) -> JsonResponse:
    pass

def WeeklyPrefPost(request, *args, **kwargs) -> JsonResponse:
    pass

def WeeklyPrefPut(request, *args, **kwargs) -> JsonResponse:
    pass

def WeeklyPrefDelete(request, *args, **kwargs) -> JsonResponse:
    pass

''' Assignments  '''

def AssignmentsGet(request, *args, **kwargs) -> JsonResponse:
    pass

def AssignmentsPost(request, *args, **kwargs) -> JsonResponse:
    pass

def AssignmentsPut(request, *args, **kwargs) -> JsonResponse:
    pass

def AssignmentsDelete(request, *args, **kwargs) -> JsonResponse:
    pass