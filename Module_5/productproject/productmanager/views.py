from django.shortcuts import render,redirect
from .forms import productForm,updateForm
from .models import products

# Create your views here.

def index(request):
    if request.method=='POST':
        user=productForm(request.POST)
        if user.is_valid():
            user.save()
            print("Your data has been saved!")
        else:
            print(user.errors)
    return render(request,'index.html')


def showdata(request):
    data=products.objects.all()
    return render(request,'showdata.html',{'data':data})

def deletedata(request,id):
    cid=products.objects.get(id=id)
    products.delete(cid)
    return redirect('showdata')

def updatedata(request,id):
    cid=products.objects.get(id=id)
    if request.method=='POST':
        updateuser=updateForm(request.POST)
        if updateuser.is_valid():
            updateuser=updateForm(request.POST,instance=cid)
            updateuser.save()
            print("Your data has been updated!")
            return redirect('showdata')
        else:
            print(updateuser.errors)
    return render(request,'updatedata.html',{'user':products.objects.get(id=id)})