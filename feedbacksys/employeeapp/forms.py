from django import forms
from django.contrib.auth.models import User, Group
from django.contrib.auth.hashers import make_password
#this securely hashes passwords before saving
from .models import SalonOwner, Stylist
from phonenumber_field.formfields import PhoneNumberField


class SalonOwnerRegistrationForm(forms.ModelForm):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    #the widgets attribute will make the passwords appear as circles instead of text
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    # second password field to ensure user has entered the correct password


    class Meta:
        model = SalonOwner
        fields = "__all__"

        labels = {
            'first_name':'',
            'last_name':'',
            'email':'',
            'phone_number':'',
            'location':'',
            'salon_name': '',
            'password':'',
            'confirm_password':'',
            
        }

        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control col-lg-4','placeholder':'Enter first name' }),#this will allow bootstrap to tyle the form
           'last_name': forms.TextInput(attrs={'class':'form-control col-lg-4', 'placeholder':'Enter last name'}),
          'email': forms.TextInput(attrs={'class':'form-control col-lg-4', 'placeholder':'Enter email address'}),
           'phone_number': forms.TextInput(attrs={'class':'form-control col-lg-4 ', 'placeholder':'Enter phone number'}),
           'location': forms.TextInput(attrs={'class':'form-control col-lg-4', 'placeholder':'Enter location of the salon'}),
           'salon_name': forms.TextInput(attrs={'class':'form-control col-lg-4 ', 'placeholder':'Enter name of salon'}),
            'password': forms.PasswordInput(attrs={'class':'form-control col-lg-4 ', 'placeholder':'Enter password'}),
            'confirm_password': forms.PasswordInput(attrs={'class':'form-control col-lg-4 ', 'placeholder':'Confirm Password'}),
        }



class StylistRegistrationForm(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    phone_number = PhoneNumberField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)


    class Meta:
        model = Stylist
        fields = "__all__"

        labels = {
            'first_name':'',
            'last_name':'',
            'email':'',
            'phone_number':'',
            'password':'',
            'confirm_password':'',
        }

        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control col-lg-4','placeholder':'Enter first name' }),#this will allow bootstrap to style the form
           'last_name': forms.TextInput(attrs={'class':'form-control col-lg-4', 'placeholder':'Enter last name'}),
          'email': forms.TextInput(attrs={'class':'form-control col-lg-4', 'placeholder':'Enter email address'}),
           'phone_number': forms.TextInput(attrs={'class':'form-control col-lg-4 ', 'placeholder':'Enter phone number'}),
           'password': forms.PasswordInput(attrs={'class':'form-control col-lg-4 ', 'placeholder':'Enter password'}),
            'confirm_password': forms.PasswordInput(attrs={'class':'form-control col-lg-4 ', 'placeholder':'Confirm Password'}),
           
        }


class StylistLoginForm(forms.ModelForm):
    first_name = forms. CharField()
    last_name = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control col-lg-4','placeholder':'Enter first name' }),#this will allow bootstrap to style the form
           'last_name': forms.TextInput(attrs={'class':'form-control col-lg-4', 'placeholder':'Enter last name'}),
           'password': forms.PasswordInput(attrs={'class':'form-control col-lg-4 ', 'placeholder':'Enter password'}),
            'confirm_password': forms.PasswordInput(attrs={'class':'form-control col-lg-4 ', 'placeholder':'Confirm Password'}),
           
        }
    


    