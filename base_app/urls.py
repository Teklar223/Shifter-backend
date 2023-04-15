from django.urls import path, include
from rest_framework import routers
from .constants import * # all id's come from here
from . import views

# TODO: is passing auto-id needed? (for example role_requisite_id)

company_patterns = [
    path(f'api/', views.CompanyView),
    path(f'api/<slug:{company_id}>/', views.CompanyView),
]

role_patterns = [
    path(f'api/<slug:{company_id}>/role/', views.RoleView),
    path(f'api/<slug:{company_id}>/role/<slug:{role_id}>/', views.RoleView),
    path(f'api/<slug:{company_id}>/rolereq/', views.RoleReqView),
    path(f'api/<slug:{company_id}>/rolereq/<slug:{role_id}>/', views.RoleReqView),
]

team_patterns = [
    path(f'api/<slug:{company_id}>/team/', views.TeamView),
    path(f'api/<slug:{company_id}>/team/<slug:{team_id}>/', views.TeamView),
    path(f'api/<slug:{company_id}>/teamreq/', views.TeamReqView),
    path(f'api/<slug:{company_id}>/teamreq/<slug:{team_id}>/', views.TeamReqView),
    path(f'api/<slug:{company_id}>/teamemp/', views.TeamEmployeeView),
    path(f'api/<slug:{company_id}>/teamemp/<slug:{team_id}>/', views.TeamEmployeeView),
]

employee_patterns = [
    path(f'api/<slug:{company_id}>/employee/', views.EmployeeView),
    path(f'api/<slug:{company_id}>/employee/<slug:{employee_id}>/', views.EmployeeView),
    path(f'api/<slug:{company_id}>/employeesup/', views.EmployeeSuperiorView),
    path(f'api/<slug:{company_id}>/employeesup/<slug:{employee_id}>/', views.EmployeeSuperiorView),
    # *****************************************TODO: ^ pass superior_id in request body?
    path(f'api/<slug:{company_id}>/employeerole/', views.EmployeeRoleView),
    path(f'api/<slug:{company_id}>/employeerole/<slug:{employee_id}>/', views.EmployeeRoleView),
]

urlpatterns = []

urlpatterns += company_patterns + role_patterns + team_patterns + employee_patterns