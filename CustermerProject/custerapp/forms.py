from django import forms
from .models import Customer, CustomerLocation

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class CustomerLocationForm(forms.ModelForm):
    class Meta:
        model = CustomerLocation
        fields = '__all__'
