from django.db import models
from datetime import datetime

# Create your models here.

class signup(models.Model):
    created=models.DateTimeField(default=datetime.now(),blank=True)
    firstname=models.CharField(max_length=25)
    lastname=models.CharField(max_length=30)
    username=models.CharField(max_length=25)
    password=models.CharField(max_length=12)
    city=models.CharField(max_length=25)
    state=models.CharField(max_length=25)
    mobile=models.BigIntegerField()
