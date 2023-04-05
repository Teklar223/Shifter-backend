from rest_framework import authentication, permissions, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from .serializers import UserSerializer
from .models import User


# Create your views here.

class BaseView(viewsets.ModelViewSet):
    # The viewsets base class provides the implementation for CRUD operations by default
    serializer_class = UserSerializer
    queryset = User.objects.all()

# TODO: currently all views allow full CRUD, change in accordance with BL (for example CompanyView might have no GET - or just a restricted GET for admins)

# ####### Company Domain ###### #
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def CompanyView(request):
    if request.method == 'GET':
        pass
    if request.method == 'POST':
        pass
    if request.method == 'PUT':
        pass
    if request.method == 'DELETE':
        pass


# ######## Role Domain ######## #
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def RoleView(request):
    if request.method == 'GET':
        pass
    if request.method == 'POST':
        pass
    if request.method == 'PUT':
        pass
    if request.method == 'DELETE':
        pass


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def RoleReqView(request):
    if request.method == 'GET':
        pass
    if request.method == 'POST':
        pass
    if request.method == 'PUT':
        pass
    if request.method == 'DELETE':
        pass


# ######## Team Domain ######## #
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def TeamView(request):
    if request.method == 'GET':
        pass
    if request.method == 'POST':
        pass
    if request.method == 'PUT':
        pass
    if request.method == 'DELETE':
        pass


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def TeamReqView(request):
    if request.method == 'GET':
        pass
    if request.method == 'POST':
        pass
    if request.method == 'PUT':
        pass
    if request.method == 'DELETE':
        pass


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def TeamEmployeeView(request):
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
def EmployeeView(request):
    if request.method == 'GET':
        pass
    if request.method == 'POST':
        pass
    if request.method == 'PUT':
        pass
    if request.method == 'DELETE':
        pass


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def EmployeeSuperiorView(request):
    if request.method == 'GET':
        pass
    if request.method == 'POST':
        pass
    if request.method == 'PUT':
        pass
    if request.method == 'DELETE':
        pass


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def EmployeeRoleView(request):
    if request.method == 'GET':
        pass
    if request.method == 'POST':
        pass
    if request.method == 'PUT':
        pass
    if request.method == 'DELETE':
        pass
