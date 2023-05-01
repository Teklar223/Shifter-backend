from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from ..constants import company_id # id's come from heres
from ..models import Company
from ..serializers import CompanySerializer

# TODO: You called this URL via PUT, but the URL doesn't end in a slash and you have APPEND_SLASH set. Django can't redirect to the slash URL while maintaining PUT data. Change your form to point to 127.0.0.1:8000/api/1/ (note the trailing slash), or set APPEND_SLASH=False in your Django settings.

def CompanyGet(request, *args, **kwargs) -> JsonResponse:
    #TODO: handle 301 (resource not found) *and then do so for all requests
    if company_id in kwargs:
        id = kwargs.get(company_id)
        company = Company.objects.get(id = id)
        serializer = CompanySerializer(company, many=False)
        return JsonResponse(serializer.data, safe=False)
    else:
        company = Company.objects.all()
        serializer = CompanySerializer(company, many=True)
        return JsonResponse(serializer.data, safe=False)
    
def CompanyPost(request, *args, **kwargs) -> JsonResponse:
    # TODO: add a 'Consistency' check
    data = JSONParser().parse(request)
    serializer = CompanySerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)

def CompanyPut(request, *args, **kwargs) -> JsonResponse:
    if company_id in kwargs:
        data = JSONParser().parse(request)
        id = kwargs.get(company_id)
        company = Company.objects.get(id = id)
        serializer = CompanySerializer(company,data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            response = serializer.data
            return JsonResponse(response, status=202)
        else:
            return JsonResponse(serializer.errors, status=500)
    else:
        return JsonResponse("Forbidenn", status=401)

def CompanyDelete(request, *args, **kwargs) -> JsonResponse:
    if company_id in kwargs:
        id = kwargs.get(company_id)
        company = Company.objects.filter(id = id)
        company.delete()
        response = "Successfully deleted 'Company' with ID="+id
        return JsonResponse(response, status=200,safe=False)
    else:
        return JsonResponse("Forbidden", status=401)
