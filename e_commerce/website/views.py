from django.shortcuts import render,redirect
from .forms import UserForm,CustomerForm,AdminForm
from django.contrib.auth import login
from .models import *
from django.db import transaction
# Create your views here.

def home(request):
    
    all_products=Product.objects.all()
    

    return render(request,'website/home.html',{'products':all_products})


@transaction.atomic
def registerCust(request):
    
    if request.method=='POST':
        metaForm=CustomerForm(request.POST)
        
        originalForm=UserForm(request.POST)
        if metaForm.is_valid() and originalForm.is_valid():
            userInstance = originalForm.save()
            customerInstance = metaForm.save(commit=False)
            customerInstance.user=userInstance
            print("Both the original user form and the customer form are valid")
            customerInstance.save()
    
            return redirect("thanks")
        else:
            print('invalid form')
    metaForm=CustomerForm()
    originalForm=UserForm()
    return render(request,'website/customerSignup.html',{'coreForm':originalForm,'customerForm':metaForm})


@transaction.atomic
def registerAdmin(request):
    
    if request.method=='POST':
        coreForm=UserForm(request.POST)
        metaForm=AdminForm(request.POST)

        if coreForm.is_valid() and metaForm.is_valid():
            print("Both of the forms are valid")
            adminInstance=metaForm.save(commit=False)
            userInstance=coreForm.save(commit=False)
            userInstance.is_superuser=True
            userInstance.is_staff=True
            userInstance.save()
            adminInstance.user=userInstance
            adminInstance.save()
        
            return redirect("thanks")
        else:
            print('invalid form')
    metaForm=AdminForm()
    originalForm=UserForm()
    return render(request,'website/adminSignup.html',{'coreForm':originalForm,'adminForm':metaForm})


def shoppingCart(request):

    return render(request,'website/shoppingCart.html')

def login(request):

    if request.method=="POST":
        pass
    return render(request,'website/login.html')
        

def thanks(request):
    return render(request,'website/thanks.html')
