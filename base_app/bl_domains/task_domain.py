from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from ..constants import role_id, company_id, error_id
from ..mongo.Models import Task
from ..mongo.constants import Task_id

''' Task  '''

def TaskGet(request, *args, **kwargs) -> JsonResponse:
    pass

def TaskPost(request, *args, **kwargs) -> JsonResponse:
    pass

def TaskPut(request, *args, **kwargs) -> JsonResponse:
    pass

def TaskDelete(request, *args, **kwargs) -> JsonResponse:
    pass