from django.urls import path, include
from rest_framework import routers
from .util import slugs
from . import views

router = routers.DefaultRouter()
router.register(r'base_app', views.BaseView, 'base_app')

'''
 note - this way of writing urls is confusing, consult the urls_draft.txt for reference
        if you need it ( located in project root - note that its a draft and not yet a 1:1)
'''

company_patterns = [

]

role_patterns = [
    path(f'api/<slug:{slugs.company_id}>/role/', views.RoleView),
    path(f'api/<slug:{slugs.company_id}>/role/<slug:{slugs.role_id}>/', views.RoleView),
    path(f'api/<slug:{slugs.company_id}>/rolereq/', views.RoleReqView),
    path(f'api/<slug:{slugs.company_id}>/rolereq/<slug:{slugs.role_id}>/', views.RoleReqView),
]

team_patterns = [

]

employee_patterns = [

]

urlpatterns = [
    path('api/', include(router.urls))
]

urlpatterns = urlpatterns + company_patterns + role_patterns + team_patterns + employee_patterns