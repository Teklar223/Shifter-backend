from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSerializer
from .models import User

# Create your views here.

class BaseView(viewsets.ModelViewSet): # The viewsets base class provides the implementation for CRUD operations by default
    serializer_class = UserSerializer
    queryset = User.objects.all()