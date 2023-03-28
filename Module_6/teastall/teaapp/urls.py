from django.contrib import admin
from django.urls import path,include
from teaapp import views

urlpatterns = [
    path('',views.index),
    path('teastore/',views.teastore, name='teastore'),
    path('cafes/',views.cafes),
    path('about/',views.about),
    path('contact/',views.contact),
    path('userlogout/',views.userlogout),
]
   