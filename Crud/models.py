from django.db import models

class Teams(models.Model):
    TeamName =  models.CharField(max_length=500)

    def __str__(self) :
        return self.TeamName

class Users(models.Model):
    UserId = models.AutoField(primary_key=True)
    password = models.CharField(max_length=500, default='password')
    UserName = models.CharField(max_length=500)
    TeamName = models.ForeignKey('Teams', on_delete=models.CASCADE)
    DateOfJoining = models.DateField()
    Role = models.CharField(max_length=500, default='Worker') 
    Admin = models.BooleanField(default=False)

    def __str__(self):
        return self.UserName  