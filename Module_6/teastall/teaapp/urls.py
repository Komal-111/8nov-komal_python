from django.contrib import admin
from django.urls import path,include
from teaapp import views

urlpatterns = [
    path('',views.index),
    path('teaservice/',views.teaservice, name='teaservice'),
    path('flavors/',views.flavors),
    path('about/',views.about),
    path('contact/',views.contact),
    #path('userlogout/',views.userlogout),
]
   