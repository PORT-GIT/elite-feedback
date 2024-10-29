from django.db import models
from location_field.models.plain import PlainLocationField
from phonenumber_field.modelfields import PhoneNumberField
from .validators import phonenumber_validation
#imports the validation code from the validation file

    
class SalonOwner(models.Model):
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=100, blank=False, unique=True)
    phone_number = PhoneNumberField(region='KE', blank=False, unique=True, validators=[phonenumber_validation])
    #extending the phonenumber django library will allow me to put regulation on the phonenumbers entered
    #like the length and the code of the number
    location = PlainLocationField(based_fields=(models.Model,), blank=False, null=False)
    salon_name = models.CharField(max_length=100, blank=False)
    
    def __str__ (self):
        return f'{self.first_name} {self.last_name}'
    

class Stylist(models.Model):
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=100, blank=False, unique=True)
    phone_number = PhoneNumberField(region='KE', blank=False, unique=True, validators=[phonenumber_validation])
    #extending the phonenumber django library will allow me to put regulation on the phonenumbers
    #entered like the length and the code of the number

    def __str__ (self):
        return f'{self.first_name} {self.last_name}'
    


    
    
    



