from django import forms
from django.contrib.auth.models import User, Group
from django.contrib.auth.hashers import make_password
from customerapp.models import Customer


class CustomerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"

        labels = {
            'first_name':'',
            'last_name':'',
            'email':'',
            'phone_number':'',
        }

        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control col-lg-4','placeholder':'Enter first name' }),#this will allow bootstrap to tyle the form
           'last_name': forms.TextInput(attrs={'class':'form-control col-lg-4', 'placeholder':'Enter last name'}),
          'email': forms.TextInput(attrs={'class':'form-control col-lg-4', 'placeholder':'Enter email address'}),
           'phone_number': forms.TextInput(attrs={'class':'form-control col-lg-4 ', 'placeholder':'Enter phone number'}),
           
        }


    