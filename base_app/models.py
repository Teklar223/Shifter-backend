from django.db import models

class User(models.Model):
    #TODO: remove (fetch something else in the frontend)
    #team_ID    =   models.ForeignKey('Team', on_delete=models.CASCADE, null=True, blank=True)
    Role        =   models.CharField(max_length=200, null=True, blank=True)
    first_name  =   models.CharField(max_length=200, null=True, blank=True)
    last_name   =   models.TextField(null=True, blank=True)

'''Assuming auto-id by the ORM '''
class Company(models.Model):
    # Company_ID
    name             =   models.CharField(max_length=200, null=True, blank=True)
    foundation_date  =   models.DateField(auto_now_add=True , null=True, blank=True)

class CompanyRoleRequisite(models.Model):
    company_ID  =   models.ForeignKey('Company', on_delete=models.CASCADE, null=True, blank=True)
    role_ID     =   models.ForeignKey('Role', on_delete=models.CASCADE, null=True, blank=True)
    requisites  =   models.IntegerField()

class Team(models.Model):
    # team_ID
    company_ID  =   models.ForeignKey('Company', on_delete=models.CASCADE, null=True, blank=True)
    name        =   models.TextField(default="New Team",null=True, blank=True)

class TeamRoleRequisites(models.Model):
    # auto_ID
    team_ID     =   models.ForeignKey('Team', on_delete=models.CASCADE, null=True, blank=True)
    role_ID     =   models.ForeignKey('Role', on_delete=models.CASCADE, null=True, blank=True)
    requisites  =   models.IntegerField()


class Role(models.Model):
    # role_ID
    company_ID      =   models.ForeignKey('Company', on_delete=models.CASCADE, null=True, blank=True)
    name            =   models.CharField(max_length=200, null=True, blank=True)
    description     =   models.CharField(max_length=200, null=True, blank=True)

class TeamEmployee(models.Model):
    # auto_ID
    team_ID     =   models.ForeignKey('Team', on_delete=models.CASCADE, null=True, blank=True)
    employee_ID =   models.ForeignKey('Employee', on_delete=models.CASCADE, null=True, blank=True)
    start_date  =   models.DateField(blank=False, null=False)
    end_date    =   models.DateField(blank=True, null=True)

class Employee(models.Model):
    # Employee_ID
    first_name  =   models.CharField(max_length=200, null=True, blank=True)
    last_name   =   models.CharField(max_length=200, null=True, blank=True)
    birthday    =   models.DateField(auto_now_add=True, null=True, blank=True)

class EmployeeSuperior(models.Model):
    employee_ID = models.OneToOneField('Employee', on_delete=models.CASCADE, null=True, blank=True)
    superior_ID = models.ForeignKey('Employee', on_delete=models.CASCADE, related_name='superior', null=True, blank=True)

class EmployeeRole(models.Model):
    employee_ID = models.ForeignKey('Employee', on_delete=models.CASCADE, null=True, blank=True)
    role_ID     = models.ForeignKey('Role', on_delete=models.CASCADE, null=True, blank=True)

        