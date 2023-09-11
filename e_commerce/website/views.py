import json
from django.contrib.auth import authenticate,login
from django.shortcuts import render,redirect
from .forms import UserForm,CustomerForm,AdminForm,LoginForm
from .models import *
from django.contrib import messages
from django.db import transaction
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
# Create your views here.

def home(request):
    
    all_products=Product.objects.all()
    

    return render(request,'website/home.html',{'products':all_products})


def renderMen(request):
    menProducts=Product.objects.filter(category__name="Men")
    return render(request,'website/womenPage.html',{'products':menProducts})

def renderWomen(request):
    womenProducts=Product.objects.filter(category__name="Women")
    return render(request,'website/womenPage.html',{'products':womenProducts})


def renderKids(request):
    kidsProducts=Product.objects.filter(category__name="Kids")
    return render(request,'website/kidsPage.html',{'products':kidsProducts})



@transaction.atomic
def registerCust(request):
    
    if request.method=='POST':
        metaForm=CustomerForm(request.POST)
        
        originalForm=UserForm(request.POST)
        if metaForm.is_valid() and originalForm.is_valid():
            userInstance = originalForm.save()
            customerInstance = metaForm.save(commit=False)
            login(request,userInstance)
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

@csrf_exempt
@login_required(login_url='login')
@transaction.atomic
def shoppingCart(request):
    if request.method=="POST":
        # this array will contain the payload that will get passed to the front end that informs the user
        # of the status of his transaction
        feedbackMessages=[]
        try:
            # this new dictionary will be used to update the products table if the data of the shopping cart is valid
            cartTotal=0
            productUpdates=[]
            productInfo={'name':'','quantity':''}
            shoppingCart=json.loads(request.body.decode('utf-8'))
            for product in shoppingCart:
                cartTotal+=float(product['product_price'])
                prod=Product.objects.get(nameEn=product['product_name'])
                if int(prod.stockQuantity>int(product['product_quantity'])):
                
                    productInfo['name']=product['product_name']
                    productInfo['quantity']=int(prod.stockQuantity)-int(product['product_quantity'])
                    productUpdates.append(productInfo)

                else:
                    msg=f'The {str(prod.nameEn)} product is out of stock.'
                    feedbackMessages.append(msg)

# After this loop finishes executing, I now have the product updates list with the entire
# quantity updates to each product


            if len(feedbackMessages)>0:
                return render(request,'website/shoppingCart.html',{'feedback':feedbackMessages})
            
            # if there were cases where the product quantity of the db product less than the quantity
# that was ordered by the customer. Then there will be a list of feedback messages that will
# displayed to the user
            
            else:
                # This loop is going to handle the updating of the products
                try:
                    for singleProduct in productUpdates:
                        newProd=Product.objects.get(nameEn=singleProduct['name'])
                        newProd.stockQuantity=singleProduct['quantity']
                        newProd.save()
                except:
                     raise ValueError("The products could not update successfully")
            
                # The products have been updated successfully
                # now, order table is going to get populated
                # retrieving the id of the user first
                usr,userOrder='',''
                # I should add functionality to validate if the user is a customer or not
                print(request.user.username)
                try:
                    
                    usr=Customer.objects.get(user__username=request.user.username)
                    userOrder=Order(customer=usr,status='Pending',totalPrice=cartTotal)
                    userOrder.save()
                except:
                    
                    raise ValueError("The order couldn't be made successfully")

                # going to update the order details

                try:
                    for singleOrder in shoppingCart:
                        singleProduct=Product.objects.get(nameEn=singleOrder['product_name'])
                        OrderDetail=OrderDetails(product=singleProduct,order=userOrder,orderedCount=singleOrder['product_quantity'])
                        OrderDetail.save()
                except:
                    raise ValueError("The order details table was not populated correctly.")
                
            
        except json.JSONDecodeError as e:
            return JsonResponse({'message':'Invalid JSON data'},status=400)
        
        return redirect('orderConfirmation')
        

    return render(request,'website/shoppingCart.html')


def orderConfirmView(request):
    return render(request,'website/orderConfirm.html')

def loginView(request):
    if request.method=="POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            userName=form.cleaned_data.get('username')
            passwd=form.cleaned_data.get('password')
        user = authenticate(request,username=userName,password=passwd)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error('That user is not registered in the db.')

    form=LoginForm()
    return render(request,'website/login.html',{'form':form})
        

def thanks(request):
    return render(request,'website/thanks.html')
