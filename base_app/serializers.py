from rest_framework import serializers
from .models import *

''' User '''


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__" # TODO: has to hide password!

''' Company '''

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"

''' Role '''

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = "__all__"

class RoleRequisiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyRoleRequisite
        fields = "__all__"

''' Team '''

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = "__all__"

class TeamRequisiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamRoleRequisites
        fields = "__all__"

class TeamEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamEmployee
        fields = "__all__"

''' Employee '''

class EmployeeSuperiorSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeSuperior
        fields = "__all__"

class EmployeeRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeRole
        fields = "__all__"