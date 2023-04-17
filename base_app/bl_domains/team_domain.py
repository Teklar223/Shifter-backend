from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from ..constants import team_id
from ..models import Team,TeamEmployee,TeamRoleRequisites
from ..serializers import TeamSerializer, TeamEmployeeSerializer, TeamRequisiteSerializer

''' Team  '''

def TeamGet(request, *args, **kwargs) -> JsonResponse:
    pass

def TeamPost(request, *args, **kwargs) -> JsonResponse:
    pass

def TeamPut(request, *args, **kwargs) -> JsonResponse:
    pass

def TeamDelete(request, *args, **kwargs) -> JsonResponse:
    pass

''' Team Requisite '''

def TeamRequisiteGet(request, *args, **kwargs) -> JsonResponse:
    pass

def TeamRequisitePost(request, *args, **kwargs) -> JsonResponse:
    pass

def TeamRequisitePut(request, *args, **kwargs) -> JsonResponse:
    pass

def TeamRequisiteDelete(request, *args, **kwargs) -> JsonResponse:
    pass

''' Team Employee '''

def TeamEmployeeGet(request, *args, **kwargs) -> JsonResponse:
    pass

def TeamEmployeePost(request, *args, **kwargs) -> JsonResponse:
    pass

def TeamEmployeePut(request, *args, **kwargs) -> JsonResponse:
    pass

def TeamEmployeeDelete(request, *args, **kwargs) -> JsonResponse:
    pass