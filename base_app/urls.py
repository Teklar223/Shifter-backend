from django.urls import path
from rest_framework.authtoken import views as auth_views
from base_app.constants import * # all id's come from here
from base_app import views

auth_patterns = [
    path('api/token-auth/', auth_views.obtain_auth_token)
]

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
    path(f'api/<slug:{company_id}>/employeerole/', views.EmployeeRoleView),
    path(f'api/<slug:{company_id}>/employeerole/<slug:{employee_id}>/', views.EmployeeRoleView),
]

task_patterns =[] # TODO

shift_patterns = [
    path(f'api/<slug:{company_id}>/shifts/', views.ShiftsView),
    path(f'api/<slug:{company_id}>/shifts/<slug:{team_id}>/', views.ShiftsView),
    path(f'api/<slug:{company_id}>/weeklypref/', views.WeeklyPrefView),
    path(f'api/<slug:{company_id}>/weeklypref/<slug:{employee_id}>/', views.WeeklyPrefView),
]

urlpatterns = [] + auth_patterns

urlpatterns += company_patterns + role_patterns + team_patterns + employee_patterns + shift_patterns + task_patterns
