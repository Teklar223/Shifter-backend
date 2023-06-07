from django.urls import path
from rest_framework.authtoken import views as auth_views
from .constants import * # all id's come from here
from . import views

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
    #Shifts
    path(f'api/<slug:{company_id}>/shifts/', views.ShiftsView),
    # path(f'api/<slug:{company_id}>/shifts/<slug:{team_id}>/', views.ShiftsView),
    path(f'api/<slug:{company_id}>/shifts/<slug:{shift_id}>/', views.ShiftsView),

    #WeeklyPref
    path(f'api/<slug:{company_id}>/weeklypref/', views.WeeklyPrefView),
    path(f'api/<slug:{company_id}>/weeklypref/<slug:{employee_id}>/', views.WeeklyPrefView),
    path(f'api/<slug:{company_id}>/weeklypref/<slug:{team_id}>/', views.WeeklyPrefView),

    #Assignments
    path(f'api/<slug:{company_id}>/assignments/', views.AssignmentsView),
    path(f'api/<slug:{company_id}>/assignments/<slug:{shift_id}>/', views.AssignmentsView),
    path(f'api/<slug:{company_id}>/assignments/<slug:{team_id}>/', views.AssignmentsView),
    path(f'api/<slug:{company_id}>/assignments/<slug:{team_id}>/', views.AssignmentsView),

    #Templates
    path(f'api/<slug:{company_id}>/shift-templates/', views.ShiftTemplateView),
    path(f'api/<slug:{company_id}>/shift-templates/<slug:{team_id}>/', views.ShiftTemplateView),
    path(f'api/<slug:{company_id}>/shift-templates/<slug:{template_id}>/', views.ShiftTemplateView),

    #Scheduling Algorithm
    path(f'api/<slug:{company_id}>/algorithm/', views.AlgorithmView)


]

urlpatterns = [] + auth_patterns

urlpatterns += company_patterns + role_patterns + team_patterns + employee_patterns + shift_patterns + task_patterns
