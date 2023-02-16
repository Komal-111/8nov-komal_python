from django.contrib import admin
from django.db.models import Model
from .models import stud
from .models import usersignup

# Register your models here.
class studsAdmin(admin.ModelAdmin):
    list_display=['firstname','city', ]

admin.site.register(stud)
admin.site.register(usersignup)
