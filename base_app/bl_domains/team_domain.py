from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from ..constants import team_id, employee_id, company_id, role_id, error_id
from ..models import Team,TeamEmployee,TeamRoleRequisites
from ..serializers import TeamSerializer, TeamEmployeeSerializer, TeamRequisiteSerializer
from ..util import prints_args_kwargs # TODO: rm

''' Team  '''

def TeamGet(request, *args, **kwargs) -> JsonResponse:
    if team_id in kwargs:
        team = Team.objects.get(id = kwargs.get(team_id, error_id), company_id= kwargs.get(company_id, error_id))
        serializer = TeamSerializer(team, many=False)
        return JsonResponse(serializer.data, safe=False)
    else:
        team = Team.objects.all()
        serializer = TeamSerializer(team, many=True)
        return JsonResponse(serializer.data, safe=False)

def TeamPost(request, *args, **kwargs) -> JsonResponse:
    data = JSONParser().parse(request)
    serializer = TeamSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)

def TeamPut(request, *args, **kwargs) -> JsonResponse:
    pass

def TeamDelete(request, *args, **kwargs) -> JsonResponse:
    pass

''' Team Requisite '''

def TeamRequisiteGet(request, *args, **kwargs) -> JsonResponse:
    if team_id in kwargs:
        teamReq = TeamRoleRequisites.objects.get(team_id = kwargs.get(team_id, error_id), role_id= request.GET.get(role_id))
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
    pass

def TeamRequisiteDelete(request, *args, **kwargs) -> JsonResponse:
    pass

''' Team Employee '''

def TeamEmployeeGet(request, *args, **kwargs) -> JsonResponse:
    if team_id in kwargs:
        teamEmp = TeamEmployee.objects.get(team_id = kwargs.get(team_id, error_id), employee_id = request.GET.get(employee_id))
        serializer = TeamEmployeeSerializer(teamEmp, many=False)
        return JsonResponse(serializer.data, safe=False)
    else:
        teamEmp = TeamEmployee.objects.all()
        serializer = TeamEmployeeSerializer(teamEmp, many=True)
        return JsonResponse(serializer.data, safe=False)
    

def TeamEmployeePost(request, *args, **kwargs) -> JsonResponse:
    data = JSONParser().parse(request)
    serializer = TeamEmployeeSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)

def TeamEmployeePut(request, *args, **kwargs) -> JsonResponse:
    pass

def TeamEmployeeDelete(request, *args, **kwargs) -> JsonResponse:
    pass