from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

''' USER '''

class CustomUserManager(BaseUserManager):

    def create_user(self, email, password, company_id = None , employee_id = None, team_id = None , role_name = None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(email = self.normalize_email(email))

        user.set_password(password)
        user.save(using = self._db)
        return user
        
    def create_superuser(self, email, password=None):
        user = self.create_user(email = email,  password = password )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractUser):
    username = None # this allows email to act as a UID
    email = models.EmailField(unique=True)
    # first_name (inherited)
    # last_name  (inherited)
    role_name = None
    # TODO: Add image API   

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] # important


''' auto-id by the ORM '''
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

        