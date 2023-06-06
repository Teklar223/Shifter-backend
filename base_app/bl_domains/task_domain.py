from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from base_app.constants import role_id, company_id, error_id
from base_app.mongo.Models import Task
from base_app.mongo.constants import Task_id

''' Task  '''

def TaskGet(request, *args, **kwargs) -> JsonResponse:
    pass

def TaskPost(request, *args, **kwargs) -> JsonResponse:
    pass

def TaskPut(request, *args, **kwargs) -> JsonResponse:
    pass

def TaskDelete(request, *args, **kwargs) -> JsonResponse:
    pass