from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from ..constants import role_id, company_id, error_id
from ..mongo.Models import Shift,DailyPref,WeeklyPref,Schedule
from ..mongo.constants import task_id

''' Shifts  '''

def ShiftsGet(request, *args, **kwargs) -> JsonResponse:
    pass

def ShiftsPost(request, *args, **kwargs) -> JsonResponse:
    pass

def ShiftsPut(request, *args, **kwargs) -> JsonResponse:
    pass

def ShiftsDelete(request, *args, **kwargs) -> JsonResponse:
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