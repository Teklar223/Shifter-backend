from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from ..constants import role_id, company_id, error_id
from ..models import Role, CompanyRoleRequisite
from ..serializers import RoleSerializer, RoleRequisiteSerializer

''' Role  '''

def RoleGet(request, *args, **kwargs) -> JsonResponse:
    if role_id in kwargs:
        role = Role.objects.get(id = kwargs.get(role_id, error_id), company_id = kwargs.get(company_id, error_id))
        serializer = RoleSerializer(role, many=False)
        return JsonResponse(serializer.data, safe=False)
    else:
        role = Role.objects.all()
        serializer = RoleSerializer(role, many=True)
        return JsonResponse(serializer.data, safe=False)

def RolePost(request, *args, **kwargs) -> JsonResponse:
    data = JSONParser().parse(request)
    serializer = RoleSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)

def RolePut(request, *args, **kwargs) -> JsonResponse:
    if role_id in kwargs:
        data = JSONParser().parse(request)
        id = kwargs.get(role_id)
        role = Role.objects.get(id = id)
        serializer = RoleSerializer(role, data = data, partial = True)
        if serializer.is_valid():
            serializer.save()
            response = serializer.data
            return JsonResponse(response, status=202)
        else:
            return JsonResponse(serializer.errors, status=500)
    else:
        return JsonResponse("Forbidenn", status=401)

def RoleDelete(request, *args, **kwargs) -> JsonResponse:
    if role_id in kwargs:
        id = kwargs.get(role_id)
        role = Role.objects.filter(id = id)
        role.delete()
        response = "Successfully deleted 'Role' with ID="+id
        return JsonResponse(response, status=200,safe=False)
    else:
        return JsonResponse("Forbidden", status=401)

''' Role Requisite '''
def RoleRequisiteGet(request, *args, **kwargs) -> JsonResponse:
    if role_id in kwargs and company_id in kwargs:
        id = kwargs.get(role_id)
        companyID = kwargs.get(company_id)
        roleReq = CompanyRoleRequisite.objects.get(role_id = id, company_id = companyID)
        serializer = RoleRequisiteSerializer(roleReq, many=False)
        return JsonResponse(serializer.data, safe=False)
    else:
        roleReq = CompanyRoleRequisite.objects.all()
        serializer = RoleRequisiteSerializer(roleReq, many=True)
        return JsonResponse(serializer.data, safe=False)

def RoleRequisitePost(request, *args, **kwargs) -> JsonResponse:
    data = JSONParser().parse(request)
    serializer = RoleRequisiteSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)

def RoleRequisitePut(request, *args, **kwargs) -> JsonResponse:
    if role_id in kwargs and company_id in kwargs:
        data = JSONParser().parse(request)
        id = kwargs.get(role_id)
        companyID = kwargs.get(company_id)
        roleReq = CompanyRoleRequisite.objects.get(role_id = id, company_id = companyID)
        serializer = RoleRequisiteSerializer(roleReq, data = data, partial = True)
        if serializer.is_valid():
            serializer.save()
            response = serializer.data
            return JsonResponse(response, status=202)
        else:
            return JsonResponse(serializer.errors, status=500)
    else:
        return JsonResponse("Forbidden", status=401)

def RoleRequisiteDelete(request, *args, **kwargs) -> JsonResponse:
    if role_id in kwargs and company_id in kwargs:
        id = kwargs.get(role_id)
        companyID = kwargs.get(company_id)
        teamEmp = CompanyRoleRequisite.objects.filter(role_id = id, company_id = companyID)
        teamEmp.delete()
        response = "Successfully deleted 'Role Requisite from company'"
        return JsonResponse(response, status=200,safe=False)
    else:
        return JsonResponse("Forbidden", status=401)