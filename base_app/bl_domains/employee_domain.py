from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from ..constants import employee_id
from ..models import Employee,EmployeeSuperior,EmployeeRole
from ..serializers import EmployeeSerializer, EmployeeSuperiorSerializer, EmployeeRoleSerializer

''' Employee  '''

def EmployeeGet(request, *args, **kwargs) -> JsonResponse:
    pass

def EmployeePost(request, *args, **kwargs) -> JsonResponse:
    pass

def EmployeePut(request, *args, **kwargs) -> JsonResponse:
    pass

def EmployeeDelete(request, *args, **kwargs) -> JsonResponse:
    pass

''' Employee Superior '''

def EmployeeSuperiorGet(request, *args, **kwargs) -> JsonResponse:
    pass

def EmployeeSuperiorPost(request, *args, **kwargs) -> JsonResponse:
    pass

def EmployeeSuperiorPut(request, *args, **kwargs) -> JsonResponse:
    pass

def EmployeeSuperiorDelete(request, *args, **kwargs) -> JsonResponse:
    pass

''' Employee Role '''

def EmployeeRoleGet(request, *args, **kwargs) -> JsonResponse:
    pass

def EmployeeRolePost(request, *args, **kwargs) -> JsonResponse:
    pass

def EmployeeRolePut(request, *args, **kwargs) -> JsonResponse:
    pass

def EmployeeRoleDelete(request, *args, **kwargs) -> JsonResponse:
    pass