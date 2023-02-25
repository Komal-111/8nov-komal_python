from django.db import models

# Create your models here.
class productadmin(models.Model):
    productname=models.CharField(max_length=50)