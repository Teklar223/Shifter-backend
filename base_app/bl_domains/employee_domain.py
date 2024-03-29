from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from base_app.constants import employee_id, superior_id, company_id, error_id, role_id
from base_app.models import EmployeeSuperior,EmployeeRole, CustomUser as Employee, Role, Team
from base_app.serializers import EmployeeSerializer, EmployeeSuperiorSerializer, EmployeeRoleSerializer

''' Employee  '''

def EmployeeGet(request, *args, **kwargs) -> JsonResponse:
    '''
    Employee = CustomerUser
    '''
    employee = request.user
    serializer = EmployeeSerializer(employee, many=False)
    data = serializer.data

    # Append the role name based on the user's role_id
    role_id = data.get('role_id')
    if role_id:
        role = Role.objects.filter(id=role_id).first()
        if role:
            data['role_name'] = role.name
        else:
            data['role_name'] = ""

    # Append a list of all team IDs where manager.id = user.id
    team_ids = Team.objects.filter(manager=employee).values_list('id', flat=True)
    data['team_ids'] = list(team_ids)

    return JsonResponse(data, safe=False)

def EmployeePost(request, *args, **kwargs) -> JsonResponse:
    data = JSONParser().parse(request)
    serializer = EmployeeSerializer(data=data)
    if serializer.is_valid():
        user: Employee = serializer.save()
        user.set_password(data["password"])
        user.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)

def EmployeePut(request, *args, **kwargs) -> JsonResponse:
    if employee_id in kwargs:
        data = JSONParser().parse(request)
        id = kwargs.get(employee_id)
        employee = Employee.objects.get(id = id)
        serializer = EmployeeSerializer(employee, data = data, partial = True)
        if serializer.is_valid():
            serializer.save()
            response = serializer.data
            return JsonResponse(response, status=202)
        else:
            return JsonResponse(serializer.errors, status=500)
    else:
        return JsonResponse("Forbidenn", status=401)

def EmployeeDelete(request, *args, **kwargs) -> JsonResponse:
    if employee_id in kwargs:
        id = kwargs.get(employee_id)
        employee = Employee.objects.filter(id = id)
        employee.delete()
        response = "Successfully deleted 'Employee' with ID="+id
        return JsonResponse(response, status=200,safe=False)
    else:
        return JsonResponse("Forbidden", status=401)

''' Employee Superior '''

def EmployeeSuperiorGet(request, *args, **kwargs) -> JsonResponse:
    superiorID = request.GET.get(employee_id) # Query
    if employee_id in kwargs or superiorID is not None:
        id = kwargs.get(employee_id)
        employeeSup = EmployeeSuperior.objects.get(employee_id = id, superior_id = superiorID)
        serializer = EmployeeSuperiorSerializer(employeeSup, many=False)
        return JsonResponse(serializer.data, safe=False)
    else:
        employeeSup = EmployeeSuperior.objects.all()
        serializer = EmployeeSuperiorSerializer(employeeSup, many=True)
        return JsonResponse(serializer.data, safe=False)

def EmployeeSuperiorPost(request, *args, **kwargs) -> JsonResponse:
    data = JSONParser().parse(request)
    serializer = EmployeeSuperiorSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)

def EmployeeSuperiorPut(request, *args, **kwargs) -> JsonResponse:
    superiorID = request.PUT.get(superior_id) # Query
    if employee_id in kwargs:
        data = JSONParser().parse(request)
        id = kwargs.get(employee_id)
        employeeSup = EmployeeSuperior.objects.get(employee_id = id, superior_id = superiorID)
        serializer = EmployeeSuperiorSerializer(employeeSup, data = data, partial = True)
        if serializer.is_valid():
            serializer.save()
            response = serializer.data
            return JsonResponse(response, status=202)
        else:
            return JsonResponse(serializer.errors, status=500)
    else:
        return JsonResponse("Forbidden", status=401)

def EmployeeSuperiorDelete(request, *args, **kwargs) -> JsonResponse:
    superiorID = request.DELETE.get(superior_id) # Query
    if employee_id in kwargs:
        id = kwargs.get(employee_id)
        employeeSup = EmployeeSuperior.objects.filter(employee_id = id, superior_id = superiorID)
        employeeSup.delete()
        response = "Successfully 'Employee superior removed'"
        return JsonResponse(response, status=200,safe=False)
    else:
        return JsonResponse("Forbidden", status=401)

''' Employee Role '''

def EmployeeRoleGet(request, *args, **kwargs) -> JsonResponse:
    '''
        expects employee_id in kwargs and role_id in query
    '''
    roleID = request.GET.get(role_id)
    if employee_id in kwargs:
        id = kwargs.get(employee_id)
        employee = EmployeeRole.objects.get(employee_id = id, role_id = roleID)
        serializer = EmployeeRoleSerializer(employee, many=False)
        return JsonResponse(serializer.data, safe=False)
    else:
        employee = EmployeeRole.objects.all()
        serializer = EmployeeRoleSerializer(employee, many=True)
        return JsonResponse(serializer.data, safe=False)

def EmployeeRolePost(request, *args, **kwargs) -> JsonResponse:
    data = JSONParser().parse(request)
    serializer = EmployeeRoleSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)

def EmployeeRolePut(request, *args, **kwargs) -> JsonResponse:
    roleID = request.DELETE.get(role_id)
    if employee_id in kwargs:
        data = JSONParser().parse(request)
        id = kwargs.get(employee_id)
        teamEmp = EmployeeRole.objects.get(employee_id = id, role_id = roleID)
        serializer = EmployeeRoleSerializer(teamEmp, data = data, partial = True)
        if serializer.is_valid():
            serializer.save()
            response = serializer.data
            return JsonResponse(response, status=202)
        else:
            return JsonResponse(serializer.errors, status=500)
    else:
        return JsonResponse("Forbidden", status=401)

def EmployeeRoleDelete(request, *args, **kwargs) -> JsonResponse:
    roleID = request.DELETE.get(role_id)
    if employee_id in kwargs:
        id = kwargs.get(employee_id)
        employeeRole = EmployeeRole.objects.filter(employee_id = id, role_id = roleID)
        employeeRole.delete()
        response = "Successfully deleted 'Employees Role'"
        return JsonResponse(response, status=200,safe=False)
    else:
        return JsonResponse("Forbidden", status=401)