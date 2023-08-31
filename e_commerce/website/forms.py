from .models import Customer
from django.forms import ModelForm


class CustomerForm(ModelForm):
    class Meta:
        model=Customer
        fields=['username','password','phone','address']