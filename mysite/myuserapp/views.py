from django.shortcuts import render,redirect
from .forms import userForm,updateForm
from  myuserapp import views
from .models import usersignup

# Create your views here.
def index(request):
    if request.method=='POST':
        user=userForm(request.POST)
        if user.is_valid():
            user.save()
            print("success")
        else:
            print(user.errors)
    return render(request,'index.html')

def showdata(request):
    data=usersignup.objects.all()
    return render(request,'showdata.html',{'data':data})


def deletedata(request,id):
    cid=usersignup.objects.get(id=id)
    usersignup.delete(cid)
    return redirect('showdata')

def updatedata(request,id):
    cid=usersignup.objects.get(id=id)
    if request.method=='POST':
        updateuser=updateForm(request.POST)
        if updateuser.is_valid():
            updateuser=updateForm(request.POST,instance=cid)
            updateuser.save()
            print("Your data has been updated!")
            return redirect('showdata')
        else:
            print(updateuser.errors)
    return render(request,'updatedata.html',{'user':usersignup.objects.get(id=id)})


