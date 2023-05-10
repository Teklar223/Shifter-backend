from rest_framework import authentication, permissions, viewsets
from rest_framework.decorators import api_view
from .bl_domains.company_domain import *
from .bl_domains.employee_domain import *
from .bl_domains.role_domain import *
from .bl_domains.team_domain import *
from .bl_domains.task_domain import *
from .bl_domains.shifts_domain import *
from oauth2_provider.decorators import protected_resource
from .constants import user_scope,manager_scope,employer_scope,admin_scope

# ####### Company Domain ###### #

@protected_resource(scopes = [admin_scope])
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def CompanyView(request, *args, **kwargs):
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
def EmployeeView(request, *args, **kwargs):
    if request.method == 'GET':
        return EmployeeGet(request, *args, **kwargs)
    if request.method == 'POST':
        return EmployeePost(request, *args, **kwargs)
    if request.method == 'PUT':
        return EmployeePut(request, *args, **kwargs)
    if request.method == 'DELETE':
        return EmployeeDelete(request, *args, **kwargs)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
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
def AssignmentsView(request, *args, **kwargs):
    if request.method == 'GET':
        return AssignmentsGet(request, *args, **kwargs)
    if request.method == 'POST':
        return AssignmentsPost(request, *args, **kwargs)
    if request.method == 'PUT':
        return AssignmentsPut(request, *args, **kwargs)
    if request.method == 'DELETE':
        return AssignmentsDelete(request, *args, **kwargs)

# ######### Task Domain ######### #

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def TaskView(request, *args, **kwargs):
    if request.method == 'GET':
        return TaskGet(request, *args, **kwargs)
    if request.method == 'POST':
        return TaskPost(request, *args, **kwargs)
    if request.method == 'PUT':
        return TaskPut(request, *args, **kwargs)
    if request.method == 'DELETE':
        return TaskDelete(request, *args, **kwargs)
