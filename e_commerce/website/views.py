from django.shortcuts import render,redirect
from .forms import CustomerForm
from django.contrib.auth import login
# Create your views here.

def home(request):

    return render(request,'website/home.html')

def register(request):
    
    if request.method=='POST':
        form=CustomerForm(request.POST)
        if form.is_valid():
            print("The form is valid")
            user=form.save()
            login(request,user)
            return redirect("thanks")
        else:
            print('invalid form')
    form=CustomerForm()
    return render(request,'website/signup.html',{'form':form})

def login(request):

    if request.method=="POST":
        pass
    return render(request,'website/login.html')
        

def thanks(request):
    return render(request,'website/thanks.html')
