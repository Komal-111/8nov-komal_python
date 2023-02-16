from django.contrib import admin
from django.urls import path
from myuserapp import views

urlpatterns = [
    path('',views.index),
    path('showdata/',views.showdata,name='showdata'),
    path('deletedata/<int:id>/',views.deletedata),
     path('updatedata/<int:id>/',views.updatedata),
]
