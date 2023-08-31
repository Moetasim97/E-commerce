from .models import Customer
from django.forms import ModelForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth import User


class CustomerForm(ModelForm):
    class Meta:
        model=User
        fields=['username','password','phone','address']
    # hashing the passwords of users    
    def save(self,commit=True,*args,**kwargs):
        PastModel=super().save(commit=False)
        PastModel.username=self.cleaned_data.get('username').lower()
        PastModel.password=make_password(self.cleaned_data.get('password'))

        if commit:
            NewModel=PastModel
            NewModel.save()
            return NewModel