from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from ..constants import company_id # id's come from heres
from ..models import Company
from ..serializers import CompanySerializer

def CompanyGet(request, *args, **kwargs) -> JsonResponse:
    #TODO: handle 301 (resource not found)
    if company_id in kwargs:
        company = Company.objects.get(id = kwargs.get(company_id))
        serializer = CompanySerializer(company, many=False)
        return JsonResponse(serializer.data, safe=False)
    else:
        company = Company.objects.all()
        serializer = CompanySerializer(company, many=True)
        return JsonResponse(serializer.data, safe=False)
    
def CompanyPost(request, *args, **kwargs) -> JsonResponse:
    data = JSONParser().parse(request)
    serializer = CompanySerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)

def CompanyPut(request, *args, **kwargs) -> JsonResponse:
    pass

def CompanyDelete(request, *args, **kwargs) -> JsonResponse:
    pass