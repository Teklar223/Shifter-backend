from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from ..constants import role_id
from ..models import Role,CompanyRoleRequisite
from ..serializers import RoleSerializer, RoleRequisiteSerializer

''' Role  '''

def RoleGet(request, *args, **kwargs) -> JsonResponse:
    pass

def RolePost(request, *args, **kwargs) -> JsonResponse:
    pass

def RolePut(request, *args, **kwargs) -> JsonResponse:
    pass

def RoleDelete(request, *args, **kwargs) -> JsonResponse:
    pass

''' Role Requisite '''
def RoleRequisiteGet(request, *args, **kwargs) -> JsonResponse:
    pass

def RoleRequisitePost(request, *args, **kwargs) -> JsonResponse:
    pass

def RoleRequisitePut(request, *args, **kwargs) -> JsonResponse:
    pass

def RoleRequisiteDelete(request, *args, **kwargs) -> JsonResponse:
    pass