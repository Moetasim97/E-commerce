# from .models import Customer
from django.forms import ModelForm
from django import forms
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from .models import Customer,CustomAdmin



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

        
    # hashing the passwords of users    
  
        

