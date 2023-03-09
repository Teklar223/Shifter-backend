from django.db import models

# Create your models here.
class Team(models.Model):
    team_name   =   models.TextField(default="New Team",null=True, blank=True)

class User(models.Model):
    #team_ID =   models.ForeignKey('Team', on_delete=models.CASCADE, null=True, blank=True)
    Role    =   models.CharField(max_length=200, null=True, blank=True)
    f_name  =   models.CharField(max_length=200, null=True, blank=True)
    l_name  =   models.TextField(null=True, blank=True)
        