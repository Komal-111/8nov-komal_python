from django.shortcuts import render,redirect
from .forms import signupForm
from .models import signup
from django.contrib.auth import logout


# Create your views here.
def index(request):
    if request.method=='POST': 
        if request.POST.get('signup')=='signup':
            newuser=signupForm(request.POST)
            if newuser.is_valid():
                newuser.save()
                print("Signup successfully!")
            else:
                print(newuser.errors)
        elif request.POST.get("login")=="login":
            unm=request.POST['username']
            pas=request.POST['password']

            uid=signup.objects.get(username=unm)
            print("Current User:",uid.id)
            user=signup.objects.filter(username=unm,password=pas)
            if user: #true
                print("Login Successfully!")
                request.session['user']=unm 
                request.session['userid']=uid.id
                return redirect('teastore')
            else:
                print("Error! Login fail")
    
    return render(request,'index.html')


    

def teastore(request):
    user=request.session.get('user')
    return render(request,'teastore.html',{'user':user})

def cafes (request):
    return render (request,'cafes.html')
def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')


def userlogout(request):
    logout(request)
    return redirect('/')

