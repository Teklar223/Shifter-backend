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

# ####### Company Domain ###### #

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def CompanyView(request, *args, **kwargs):
    # TODO: check Auth level and proceed accordingly

    if request.method == 'GET':
        return CompanyGet(request, *args, **kwargs)
    if request.method == 'POST':
        return CompanyPost(request, *args, **kwargs)
    if request.method == 'PUT':
        return CompanyPut(request, *args, **kwargs)
    if request.method == 'DELETE':
        return CompanyDelete(request, *args, **kwargs)


# ######## Role Domain ######## #
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def RoleView(request, *args, **kwargs):
    if request.method == 'GET':
        return RoleGet(request, *args, **kwargs)
    if request.method == 'POST':
        return RolePost(request, *args, **kwargs)
    if request.method == 'PUT':
        return RolePut(request, *args, **kwargs)
    if request.method == 'DELETE':
        return RoleDelete(request, *args, **kwargs)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def RoleReqView(request, *args, **kwargs):
    if request.method == 'GET':
        return RoleRequisiteGet(request, *args, **kwargs)
    if request.method == 'POST':
        return RoleRequisitePost(request, *args, **kwargs)
    if request.method == 'PUT':
        return RoleRequisitePut(request, *args, **kwargs)
    if request.method == 'DELETE':
        return RoleRequisiteDelete(request, *args, **kwargs)


# ######## Team Domain ######## #
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def TeamView(request, *args, **kwargs):
    if request.method == 'GET':
        return TeamGet(request, *args, **kwargs)
    if request.method == 'POST':
        return TeamPost(request, *args, **kwargs)
    if request.method == 'PUT':
        return TeamPut(request, *args, **kwargs)
    if request.method == 'DELETE':
        return TeamDelete(request, *args, **kwargs)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def TeamReqView(request, *args, **kwargs):
    if request.method == 'GET':
        return TeamRequisiteGet(request, *args, **kwargs)
    if request.method == 'POST':
        return TeamRequisitePost(request, *args, **kwargs)
    if request.method == 'PUT':
        return TeamRequisitePut(request, *args, **kwargs)
    if request.method == 'DELETE':
        return TeamRequisiteDelete(request, *args, **kwargs)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def TeamEmployeeView(request, *args, **kwargs):
    if request.method == 'GET':
        return TeamEmployeeGet(request, *args, **kwargs)
    if request.method == 'POST':
        return TeamEmployeePost(request, *args, **kwargs)
    if request.method == 'PUT':
        return TeamEmployeePut(request, *args, **kwargs)
    if request.method == 'DELETE':
        return TeamEmployeeDelete(request, *args, **kwargs)


# ####### Employee Domain ####### #

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def EmployeeView(request, *args, **kwargs):
    '''
        USER view
    '''
    if request.method == 'GET':
        return EmployeeGet(request, *args, **kwargs)
    if request.method == 'POST':
        return EmployeePost(request, *args, **kwargs)
    if request.method == 'PUT':
        return EmployeePut(request, *args, **kwargs)
    if request.method == 'DELETE':
        return EmployeeDelete(request, *args, **kwargs)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def EmployeeSuperiorView(request, *args, **kwargs):
    if request.method == 'GET':
        return EmployeeSuperiorGet(request, *args, **kwargs)
    if request.method == 'POST':
        return EmployeeSuperiorPost(request, *args, **kwargs)
    if request.method == 'PUT':
        return EmployeeSuperiorPut(request, *args, **kwargs)
    if request.method == 'DELETE':
        return EmployeeSuperiorDelete(request, *args, **kwargs)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def EmployeeRoleView(request, *args, **kwargs):
    if request.method == 'GET':
        return EmployeeRoleGet(request, *args, **kwargs)
    if request.method == 'POST':
        return EmployeeRolePost(request, *args, **kwargs)
    if request.method == 'PUT':
        return EmployeeRolePut(request, *args, **kwargs)
    if request.method == 'DELETE':
        return EmployeeRoleDelete(request, *args, **kwargs)
    

# ######## Shifts Domain ######## #

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def ShiftsView(request, *args, **kwargs):
    if request.method == 'GET':
        return ShiftsGet(request, *args, **kwargs)
    if request.method == 'POST':
        return ShiftsPost(request, *args, **kwargs)
    if request.method == 'PUT':
        return ShiftsPut(request, *args, **kwargs)
    if request.method == 'DELETE':
        return ShiftsDelete(request, *args, **kwargs)
    
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def WeeklyPrefView(request, *args, **kwargs):
    if request.method == 'GET':
        return WeeklyPrefGet(request, *args, **kwargs)
    if request.method == 'POST':
        return WeeklyPrefPost(request, *args, **kwargs)
    if request.method == 'PUT':
        return WeeklyPrefPut(request, *args, **kwargs)
    if request.method == 'DELETE':
        return WeeklyPrefDelete(request, *args, **kwargs)
    
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def AssignmentsView(request, *args, **kwargs):
    if request.method == 'GET':
        return AssignmentsGet(request, *args, **kwargs)
    if request.method == 'POST':
        return AssignmentsPost(request, *args, **kwargs)
    if request.method == 'PUT':
        return AssignmentsPut(request, *args, **kwargs)
    if request.method == 'DELETE':
        return AssignmentsDelete(request, *args, **kwargs)
    
############# Shift Template Domain ##############

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def ShiftTemplateView(request, *args, **kwargs):
    if request.method == 'GET':
        return Shift_Templates_Get(request, *args, **kwargs)
    if request.method == 'POST':
        return Shift_Template_Post(request, *args, **kwargs)
    if request.method == 'PUT':
        return Shift_Template_Put(request, *args, **kwargs)
    if request.method == 'DELETE':
        return Shift_Template_Delete(request, *args, **kwargs)
    
########### Algorithm Domain ###############

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def AlgorithmView(request, *args, **kwargs):
    if request.method == 'GET':
        return SchedulingAlgorithmRun(request, *args, **kwargs)

# ######### Task Domain ######### #

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def TaskView(request, *args, **kwargs):
    if request.method == 'GET':
        return TaskGet(request, *args, **kwargs)
    if request.method == 'POST':
        return TaskPost(request, *args, **kwargs)
    if request.method == 'PUT':
        return TaskPut(request, *args, **kwargs)
    if request.method == 'DELETE':
        return TaskDelete(request, *args, **kwargs)
