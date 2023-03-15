from django.shortcuts import render,redirect
from .forms import signupForm
from .models import signup
from django.contrib.auth import logout


# Create your views here.
def index(request):
   

    return render(request,'index.html')

def teaservice(request):
    user=request.session.get('user')
    return render(request,'teaservice.html',{'user':user})

def flavors(request):
    return render(request,'flavor.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

