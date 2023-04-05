from django.urls import path, include
from rest_framework import routers
from .util import slugs
from . import views

router = routers.DefaultRouter()
router.register(r'base_app', views.BaseView, 'base_app')

'''
 note - this way of writing urls is confusing, consult the urls_draft.txt for reference
        if you need it ( located in project root)
'''

company_patterns = [

]

role_patterns = [
    path(f'api/<slug:{slugs.company_id}>/role/', views.RoleView),
    path(f'api/<slug:{slugs.company_id}>/role/<slug:{slugs.role_id}>/', views.RoleView),
    path(f'api/<slug:{slugs.company_id}>/role/req>/', views.RoleReqView),
    path(f'api/<slug:{slugs.company_id}>/role/{slugs.role_id}/req>/', views.RoleReqView),
    path(f'api/<slug:{slugs.company_id}>/role/req>/{slugs.requisite_id}/', views.RoleReqView),
    path(f'api/<slug:{slugs.company_id}>/role/{slugs.role_id}/req>/{slugs.requisite_id}/', views.RoleReqView),
]

team_patterns = [

]

employee_patterns = [

]

urlpatterns = [
    path('api/', include(router.urls))
]

urlpatterns = urlpatterns + company_patterns + role_patterns + team_patterns + employee_patterns