from django.http import HttpResponse, JsonResponse
from rest_framework import authentication, permissions, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from .serializers import *
from .constants import * # id's come from heres


# TODO: remove import
from .util import prints_args_kwargs

# ####### Company Domain ###### #
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def CompanyView(request, *args, **kwargs):
    if request.method == 'GET':
        if company_id in kwargs:
            company = Company.objects.get(id = kwargs.get(company_id))
            serializer = CompanySerializer(company, many=False)
            return JsonResponse(serializer.data, safe=False)
        else:
            company = Company.objects.all()
            serializer = CompanySerializer(company, many=True)
            return JsonResponse(serializer.data, safe=False)
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CompanySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    if request.method == 'PUT':
        pass
    if request.method == 'DELETE':
        pass


# ######## Role Domain ######## #
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def RoleView(request, *args, **kwargs):
    if request.method == 'GET':
        prints_args_kwargs(args=args,kwargs=kwargs)
        return Response("role view get")
    
    if request.method == 'POST':
        prints_args_kwargs(args=args,kwargs=kwargs)
        return Response("role view post")
    
    if request.method == 'PUT':
        prints_args_kwargs(args=args,kwargs=kwargs)
        return Response("role view put")
    
    if request.method == 'DELETE':
        prints_args_kwargs(args=args,kwargs=kwargs)
        return Response("role view delete")

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def RoleReqView(request, *args, **kwargs):
    if request.method == 'GET':
        prints_args_kwargs(args=args,kwargs=kwargs)
        return Response("role req view get")
    
    elif request.method == 'POST':
        prints_args_kwargs(args=args,kwargs=kwargs)
        return Response("role req view post")
    
    elif request.method == 'PUT':
        prints_args_kwargs(args=args,kwargs=kwargs)
        return Response("role req view put")
    
    elif request.method == 'DELETE':
        prints_args_kwargs(args=args,kwargs=kwargs)
        return Response("role req view delete")


# ######## Team Domain ######## #
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def TeamView(request, *args, **kwargs):
    if request.method == 'GET':
        pass
    if request.method == 'POST':
        pass
    if request.method == 'PUT':
        pass
    if request.method == 'DELETE':
        pass


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def TeamReqView(request, *args, **kwargs):
    if request.method == 'GET':
        pass
    if request.method == 'POST':
        pass
    if request.method == 'PUT':
        pass
    if request.method == 'DELETE':
        pass


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def TeamEmployeeView(request, *args, **kwargs):
    if request.method == 'GET':
        pass
    if request.method == 'POST':
        pass
    if request.method == 'PUT':
        pass
    if request.method == 'DELETE':
        pass


# ####### Employee Domain ####### #

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def EmployeeView(request, *args, **kwargs):
    if request.method == 'GET':
        pass
    if request.method == 'POST':
        pass
    if request.method == 'PUT':
        pass
    if request.method == 'DELETE':
        pass


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def EmployeeSuperiorView(request, *args, **kwargs):
    if request.method == 'GET':
        pass
    if request.method == 'POST':
        pass
    if request.method == 'PUT':
        pass
    if request.method == 'DELETE':
        pass


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def EmployeeRoleView(request, *args, **kwargs):
    if request.method == 'GET':
        pass
    if request.method == 'POST':
        pass
    if request.method == 'PUT':
        pass
    if request.method == 'DELETE':
        pass
