from django.contrib import admin
from .models import productadmin

# Register your models here.
class productadminadmin(admin.ModelAdmin):
    list_display=['productname']

admin.site.register(productadmin,productadminadmin)