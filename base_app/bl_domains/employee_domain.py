from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from ..constants import employee_id, superior_id, company_id, error_id, role_id
from ..models import Employee,EmployeeSuperior,EmployeeRole
from ..serializers import EmployeeSerializer, EmployeeSuperiorSerializer, EmployeeRoleSerializer

''' Employee  '''

def EmployeeGet(request, *args, **kwargs) -> JsonResponse:
    '''
    expects company_id and employee_id in kwargs, and superior_id in query
    '''
    if employee_id in kwargs:
        team = Employee.objects.get(id = kwargs.get(employee_id, error_id))
        serializer = EmployeeSerializer(team, many=False)
        return JsonResponse(serializer.data, safe=False)
    else:
        team = Employee.objects.all()
        serializer = EmployeeSerializer(team, many=True)
        return JsonResponse(serializer.data, safe=False)

def EmployeePost(request, *args, **kwargs) -> JsonResponse:
    data = JSONParser().parse(request)
    serializer = EmployeeSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)

def EmployeePut(request, *args, **kwargs) -> JsonResponse:
    pass

def EmployeeDelete(request, *args, **kwargs) -> JsonResponse:
    pass

''' Employee Superior '''

def EmployeeSuperiorGet(request, *args, **kwargs) -> JsonResponse:
    if employee_id in kwargs:
        team = EmployeeSuperior.objects.get(employee_id = kwargs.get(employee_id, error_id), superior_id = request.GET.get(employee_id))
        serializer = EmployeeSuperiorSerializer(team, many=False)
        return JsonResponse(serializer.data, safe=False)
    else:
        team = EmployeeSuperior.objects.all()
        serializer = EmployeeSuperiorSerializer(team, many=True)
        return JsonResponse(serializer.data, safe=False)

def EmployeeSuperiorPost(request, *args, **kwargs) -> JsonResponse:
    data = JSONParser().parse(request)
    serializer = EmployeeSuperiorSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)

def EmployeeSuperiorPut(request, *args, **kwargs) -> JsonResponse:
    pass

def EmployeeSuperiorDelete(request, *args, **kwargs) -> JsonResponse:
    pass

''' Employee Role '''

def EmployeeRoleGet(request, *args, **kwargs) -> JsonResponse:
    '''
        expects employee_id in kwargs and role_id in query
    '''
    if employee_id in kwargs:
        team = EmployeeRole.objects.get(employee_id = kwargs.get(employee_id, error_id), role_id = request.GET.get(role_id))
        serializer = EmployeeRoleSerializer(team, many=False)
        return JsonResponse(serializer.data, safe=False)
    else:
        team = EmployeeRole.objects.all()
        serializer = EmployeeRoleSerializer(team, many=True)
        return JsonResponse(serializer.data, safe=False)

def EmployeeRolePost(request, *args, **kwargs) -> JsonResponse:
    data = JSONParser().parse(request)
    serializer = EmployeeRoleSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)

def EmployeeRolePut(request, *args, **kwargs) -> JsonResponse:
    pass

def EmployeeRoleDelete(request, *args, **kwargs) -> JsonResponse:
    pass