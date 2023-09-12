# from .models import Customer
from django.forms import ModelForm
from django import forms
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from .models import Customer,CustomAdmin,Category
from django.forms import Form, CharField, ModelChoiceField, ChoiceField, BooleanField



ORDER_CHOICES = [
    ('PRICE_ASC', 'Price (lowest first)'),
    ('PRICE_DESC', 'Price (highest first)'),
    ('NAME', 'Name')
]

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)




class UserForm(ModelForm):
    class Meta:
        model = User
        fields=['username','password','email','first_name','last_name']


    def save(self,commit=True,*args,**kwargs):
        m=super().save(commit=False)
        m.password=make_password(self.cleaned_data.get('password'))
        m.username=self.cleaned_data.get('username').lower()
       
       


        if commit:
            m.save()
        return m

    
      

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        exclude=['user']
        fields = ['phone','address']

   
   
        
class AdminForm(ModelForm):
    class Meta:
        model = CustomAdmin
        exclude=['user']
        fields = ['jobtitle']


class FilterForm(Form):
    name = CharField(required=False)
    category = ModelChoiceField(queryset=Category.objects.all(), required=False)
    order_by = ChoiceField(choices=ORDER_CHOICES, required=False)
    only_in_stock = BooleanField(label="Only select products that are in stock.", required=False)

        
    # hashing the passwords of users    
  
        

