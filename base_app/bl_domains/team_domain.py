from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from base_app.constants import team_id, employee_id, company_id, role_id, error_id
from base_app.models import Team,TeamEmployee,TeamRoleRequisites, CustomUser as Employee
from base_app.serializers import TeamSerializer, TeamEmployeeSerializer, TeamRequisiteSerializer, EmployeeSerializer
import json

''' Team  '''

# TODO : check for company_id validity as needed

def TeamGet(request, *args, **kwargs) -> JsonResponse:        
    if request.GET.get("all"):
        print(kwargs)
        role = Team.objects.filter(company_id=kwargs["company_id"])
        serializer = TeamSerializer(role, many=True)
        return JsonResponse(serializer.data, safe=False)
    if team_id in kwargs:
        # Temporary way to get all the teams
        # TODO get by companyID
        team = Team.objects.all()
        serializer = TeamSerializer(team, many=True)
        return JsonResponse(serializer.data, safe=False)
    else:
        team_ids = []

        try:
            body = json.loads(request.body)
            team_ids = body.get('team_ids', [])
        except json.JSONDecodeError:
            pass

        data = []
        for id in team_ids:
            try:
                team = Team.objects.get(id=id)
                serializer = TeamSerializer(team)
                data.append(serializer.data)
            except Team.DoesNotExist:
                pass

        return JsonResponse(data, status=200, safe=False)
    
def TeamPost(request, *args, **kwargs) -> JsonResponse:
    data = JSONParser().parse(request)
    serializer = TeamSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)

def TeamPut(request, *args, **kwargs) -> JsonResponse:
    if team_id in kwargs:
        data = JSONParser().parse(request)
        id = kwargs.get(team_id)
        team = Team.objects.get(id = id)
        serializer = TeamSerializer(team, data = data, partial = True)
        if serializer.is_valid():
            serializer.save()
            response = serializer.data
            return JsonResponse(response, status=202)
        else:
            return JsonResponse(serializer.errors, status=500)
    else:
        return JsonResponse("Forbidenn", status=401)

def TeamDelete(request, *args, **kwargs) -> JsonResponse:
    if team_id in kwargs:
        id = kwargs.get(team_id)
        team = Team.objects.filter(id = id)
        team.delete()
        response = "Successfully deleted 'Team' with ID="+id
        return JsonResponse(response, status=200,safe=False)
    else:
        return JsonResponse("Forbidden", status=401)

''' Team Requisite '''

def TeamRequisiteGet(request, *args, **kwargs) -> JsonResponse:
    if team_id in kwargs:
        id = kwargs.get(team_id)
        roleID = request.GET.get(role_id)
        teamReq = TeamRoleRequisites.objects.get(team_id = id, role_id= roleID)
        serializer = TeamRequisiteSerializer(teamReq, many=False)
        return JsonResponse(serializer.data, safe=False)
    else:
        teamReq = TeamRoleRequisites.objects.all()
        serializer = TeamRequisiteSerializer(teamReq, many=True)
        return JsonResponse(serializer.data, safe=False)

def TeamRequisitePost(request, *args, **kwargs) -> JsonResponse:
    data = JSONParser().parse(request)
    serializer = TeamRequisiteSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)

def TeamRequisitePut(request, *args, **kwargs) -> JsonResponse:
    roleID = request.PUT.get(role_id) # Query
    if team_id in kwargs and roleID is not None:
        data = JSONParser().parse(request)
        id = kwargs.get(team_id)
        teamReq = TeamRoleRequisites.objects.get(team_id = id, role_id = roleID)
        serializer = TeamRequisiteSerializer(teamReq, data = data, partial = True)
        if serializer.is_valid():
            serializer.save()
            response = serializer.data
            return JsonResponse(response, status=202)
        else:
            return JsonResponse(serializer.errors, status=500)
    else:
        return JsonResponse("Forbidenn", status=401)

def TeamRequisiteDelete(request, *args, **kwargs) -> JsonResponse:
    roleID = request.PUT.get(role_id) # Query
    if team_id in kwargs and roleID is not None:
        id = kwargs.get(team_id)
        teamReq = TeamRoleRequisites.objects.filter(team_id = id, role_id = roleID)
        teamReq.delete()
        response = "Successfully deleted 'Team Role Requisite'"
        return JsonResponse(response, status=200,safe=False)
    else:
        return JsonResponse("Forbidden", status=401)

''' Team Employee '''

def TeamEmployeeGet(request, *args, **kwargs) -> JsonResponse:
    team_ids = []

    try:
        body = json.loads(request.body)
        team_ids = body.get('team_ids', [])
    except json.JSONDecodeError:
        pass

    data = []
    if team_ids:
        users = Employee.objects.filter(team_id__in=team_ids)
    else:
        users = Employee.objects.filter(company_id=kwargs["company_id"])
    serialized_users = EmployeeSerializer(users, many=True).data
    data.extend(serialized_users)

    return JsonResponse(data, status=200, safe=False)

    
def TeamEmployeePost(request, *args, **kwargs) -> JsonResponse:
    data = JSONParser().parse(request)
    serializer = TeamEmployeeSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)

def TeamEmployeePut(request, *args, **kwargs) -> JsonResponse:
    employeeID = request.PUT.get(employee_id) # Query
    if team_id in kwargs or employeeID is not None:
        data = JSONParser().parse(request)
        id = kwargs.get(team_id)
        teamEmp = TeamEmployee.objects.get(team_id = id, employee_id = employeeID)
        serializer = TeamEmployeeSerializer(teamEmp, data = data, partial = True)
        if serializer.is_valid():
            serializer.save()
            response = serializer.data
            return JsonResponse(response, status=202)
        else:
            return JsonResponse(serializer.errors, status=500)
    else:
        return JsonResponse("Forbidden", status=401)

def TeamEmployeeDelete(request, *args, **kwargs) -> JsonResponse:
    employeeID = request.DELETE.get(employee_id) # Query
    if team_id in kwargs or employeeID is not None:
        id = kwargs.get(team_id)
        teamEmp = TeamEmployee.objects.filter(team_id = id, employee_id = employeeID)
        teamEmp.delete()
        response = "Successfully deleted 'Employee from team'"
        return JsonResponse(response, status=200,safe=False)
    else:
        return JsonResponse("Forbidden", status=401)