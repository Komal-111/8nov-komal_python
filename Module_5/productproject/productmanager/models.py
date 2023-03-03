from django.db import models

# Create your models here.
class products(models.Model):
    productname=models.CharField(max_length=50)
    productprice=models.IntegerField()
    productrame=models.CharField(max_length=50)
    productcatagory=models.CharField(max_length=20)