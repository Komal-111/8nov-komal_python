from django.db import models

# Create your models here.
class stud(models.Model):
    firstnsame=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    mobilenumber=models.BigIntegerField()
    emailid=models.EmailField()


    def __str__(self):
        return self.firstnsame,self.city
class usersignup(models.Model):
    username=models.CharField(max_length=50)
    passward=models.CharField(max_length=50)


    def __str__(self) -> str:
        return self.username
        
  