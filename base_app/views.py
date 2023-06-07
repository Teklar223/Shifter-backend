from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from base_app.bl_domains.company_domain import *
from base_app.bl_domains.employee_domain import *
from base_app.bl_domains.role_domain import *
from base_app.bl_domains.team_domain import *
from base_app.bl_domains.task_domain import *
from base_app.bl_domains.shifts_domain import *
from base_app.constants import user_scope,manager_scope,employer_scope,admin_scope

# HTTP Method constants

GET = 'GET'
POST = 'POST'
PUT = 'PUT'
PATCH = 'PATCH'
DELETE = 'DELETE'

# ####### Company Domain ###### #

@api_view([PUT, POST, PATCH, DELETE])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def CompanyView(request, *args, **kwargs):
    # TODO: check Auth level and proceed accordingly

    if request.method == PUT:
        return CompanyGet(request, *args, **kwargs)
    if request.method == POST:
        return CompanyPost(request, *args, **kwargs)
    if request.method == PATCH:
        return CompanyPut(request, *args, **kwargs)
    if request.method == DELETE:
        return CompanyDelete(request, *args, **kwargs)


# ######## Role Domain ######## #
@api_view([PUT, POST, PATCH, DELETE])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def RoleView(request, *args, **kwargs):
    if request.method == PUT:
        return RoleGet(request, *args, **kwargs)
    if request.method == POST:
        return RolePost(request, *args, **kwargs)
    if request.method == PATCH:
        return RolePut(request, *args, **kwargs)
    if request.method == DELETE:
        return RoleDelete(request, *args, **kwargs)

@api_view([PUT, POST, PATCH, DELETE])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def RoleReqView(request, *args, **kwargs):
    if request.method == PUT:
        return RoleRequisiteGet(request, *args, **kwargs)
    if request.method == POST:
        return RoleRequisitePost(request, *args, **kwargs)
    if request.method == PATCH:
        return RoleRequisitePut(request, *args, **kwargs)
    if request.method == DELETE:
        return RoleRequisiteDelete(request, *args, **kwargs)


# ######## Team Domain ######## #
@api_view([PUT, POST, PATCH, DELETE])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def TeamView(request, *args, **kwargs):
    if request.method == PUT:
        return TeamGet(request, *args, **kwargs)
    if request.method == POST:
        return TeamPost(request, *args, **kwargs)
    if request.method == PATCH:
        return TeamPut(request, *args, **kwargs)
    if request.method == DELETE:
        return TeamDelete(request, *args, **kwargs)


@api_view([PUT, POST, PATCH, DELETE])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def TeamReqView(request, *args, **kwargs):
    if request.method == PUT:
        return TeamRequisiteGet(request, *args, **kwargs)
    if request.method == POST:
        return TeamRequisitePost(request, *args, **kwargs)
    if request.method == PATCH:
        return TeamRequisitePut(request, *args, **kwargs)
    if request.method == DELETE:
        return TeamRequisiteDelete(request, *args, **kwargs)


@api_view([PUT, POST, PATCH, DELETE])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def TeamEmployeeView(request, *args, **kwargs):
    if request.method == PUT:
        return TeamEmployeeGet(request, *args, **kwargs)
    if request.method == POST:
        return TeamEmployeePost(request, *args, **kwargs)
    if request.method == PATCH:
        return TeamEmployeePut(request, *args, **kwargs)
    if request.method == DELETE:
        return TeamEmployeeDelete(request, *args, **kwargs)


# ####### Employee Domain ####### #

@api_view([PUT, POST, PATCH, DELETE])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def EmployeeView(request, *args, **kwargs):
    '''
        USER view
    '''
    if request.method == PUT:
        return EmployeeGet(request, *args, **kwargs)
    if request.method == POST:
        return EmployeePost(request, *args, **kwargs)
    if request.method == PATCH:
        return EmployeePut(request, *args, **kwargs)
    if request.method == DELETE:
        return EmployeeDelete(request, *args, **kwargs)


@api_view([PUT, POST, PATCH, DELETE])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def EmployeeSuperiorView(request, *args, **kwargs):
    if request.method == PUT:
        return EmployeeSuperiorGet(request, *args, **kwargs)
    if request.method == POST:
        return EmployeeSuperiorPost(request, *args, **kwargs)
    if request.method == PATCH:
        return EmployeeSuperiorPut(request, *args, **kwargs)
    if request.method == DELETE:
        return EmployeeSuperiorDelete(request, *args, **kwargs)


@api_view([PUT, POST, PATCH, DELETE])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def EmployeeRoleView(request, *args, **kwargs):
    if request.method == PUT:
        return EmployeeRoleGet(request, *args, **kwargs)
    if request.method == POST:
        return EmployeeRolePost(request, *args, **kwargs)
    if request.method == PATCH:
        return EmployeeRolePut(request, *args, **kwargs)
    if request.method == DELETE:
        return EmployeeRoleDelete(request, *args, **kwargs)
    

# ######## Shifts Domain ######## #

@api_view([PUT, POST, PATCH, DELETE])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def ShiftsView(request, *args, **kwargs):
    if request.method == PUT:
        return ShiftsGet(request, *args, **kwargs)
    if request.method == POST:
        return ShiftsPost(request, *args, **kwargs)
    if request.method == PATCH:
        return ShiftsPut(request, *args, **kwargs)
    if request.method == DELETE:
        return ShiftsDelete(request, *args, **kwargs)
    
@api_view([PUT, POST, PATCH, DELETE])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def WeeklyPrefView(request, *args, **kwargs):
    if request.method == PUT:
        return WeeklyPrefGet(request, *args, **kwargs)
    if request.method == POST:
        return WeeklyPrefPost(request, *args, **kwargs)
    if request.method == PATCH:
        return WeeklyPrefPut(request, *args, **kwargs)
    if request.method == DELETE:
        return WeeklyPrefDelete(request, *args, **kwargs)
    
@api_view([PUT, POST, PATCH, DELETE])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def AssignmentsView(request, *args, **kwargs):
    if request.method == PUT:
        return AssignmentsGet(request, *args, **kwargs)
    if request.method == POST:
        return AssignmentsPost(request, *args, **kwargs)
    if request.method == PATCH:
        return AssignmentsPut(request, *args, **kwargs)
    if request.method == DELETE:
        return AssignmentsDelete(request, *args, **kwargs)
    
############# Shift Template Domain ##############

@api_view([PUT, POST, PATCH, DELETE])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def ShiftTemplateView(request, *args, **kwargs):
    if request.method == PUT:
        return Shift_Templates_Get(request, *args, **kwargs)
    if request.method == POST:
        return Shift_Template_Post(request, *args, **kwargs)
    if request.method == PATCH:
        return Shift_Template_Put(request, *args, **kwargs)
    if request.method == DELETE:
        return Shift_Template_Delete(request, *args, **kwargs)
    
########### Algorithm Domain ###############

@api_view([PUT])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def AlgorithmView(request, *args, **kwargs):
    if request.method == PUT:
        return SchedulingAlgorithmRun(request, *args, **kwargs)

# ######### Task Domain ######### #

@api_view([PUT, POST, PATCH, DELETE])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def TaskView(request, *args, **kwargs):
    if request.method == PUT:
        return TaskGet(request, *args, **kwargs)
    if request.method == POST:
        return TaskPost(request, *args, **kwargs)
    if request.method == PATCH:
        return TaskPut(request, *args, **kwargs)
    if request.method == DELETE:
        return TaskDelete(request, *args, **kwargs)
