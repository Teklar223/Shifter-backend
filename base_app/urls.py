from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'base_app', views.BaseView, 'base_app')
router.register(r'base_app',views.CompanyView,'company_view')

urlpatterns = [
    path('api/', include(router.urls)),
]