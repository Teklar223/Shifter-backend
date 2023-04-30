from django.db import models

'''Assuming auto-id by the ORM '''
class Company(models.Model):
    # id
    name             =   models.CharField(max_length=200, null=True, blank=True)
    foundation_date  =   models.DateField(auto_now_add=True , null=True, blank=True)

class Role(models.Model):
    # id
    company_id      =   models.ForeignKey('Company', on_delete=models.CASCADE, null=True, blank=True)
    name            =   models.CharField(max_length=200, null=True, blank=True)
    description     =   models.CharField(max_length=200, null=True, blank=True)

class CompanyRoleRequisite(models.Model):
    # id
    company_id  =   models.ForeignKey('Company', on_delete=models.CASCADE, null=True, blank=True)
    role_id     =   models.ForeignKey('Role', on_delete=models.CASCADE, null=True, blank=True)
    requisites  =   models.IntegerField()

class Team(models.Model):
    # id
    company_id  =   models.ForeignKey('Company', on_delete=models.CASCADE, null=True, blank=True)
    name        =   models.TextField(default="New Team",null=True, blank=True)

class TeamRoleRequisites(models.Model):
    # id
    team_id     =   models.ForeignKey('Team', on_delete=models.CASCADE, null=True, blank=True)
    role_id     =   models.ForeignKey('Role', on_delete=models.CASCADE, null=True, blank=True)
    requisites  =   models.IntegerField()


class TeamEmployee(models.Model):
    # id
    team_id     =   models.ForeignKey('Team', on_delete=models.CASCADE, null=True, blank=True)
    employee_id =   models.ForeignKey('Employee', on_delete=models.CASCADE, null=True, blank=True)
    start_date  =   models.DateField(blank=False, null=False)
    end_date    =   models.DateField(blank=True, null=True)

class Employee(models.Model):
    # id
    first_name  =   models.CharField(max_length=200, null=True, blank=True)
    last_name   =   models.CharField(max_length=200, null=True, blank=True)
    birthday    =   models.DateField(auto_now_add=True, null=True, blank=True)

class EmployeeSuperior(models.Model):
    # id
    employee_id = models.OneToOneField('Employee', on_delete=models.CASCADE, null=True, blank=True)
    superior_id = models.ForeignKey('Employee', on_delete=models.CASCADE, related_name='superior', null=True, blank=True)

class EmployeeRole(models.Model):
    # id
    employee_id = models.ForeignKey('Employee', on_delete=models.CASCADE, null=True, blank=True)
    role_id     = models.ForeignKey('Role', on_delete=models.CASCADE, null=True, blank=True)

        