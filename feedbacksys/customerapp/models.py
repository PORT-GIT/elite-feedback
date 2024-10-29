from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from employeeapp.validators import phonenumber_validation


# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(blank=False, max_length=50)
    last_name = models.CharField(blank=True, max_length=50)
    email = models.EmailField(max_length=100, blank=False, unique=True)
    phone_number = PhoneNumberField(region='KE', blank=False, unique=True, validators=[phonenumber_validation])
    date_joined = models.DateField(auto_now_add=True)

    def __str__ (self):
        return self.first_name + "   " + self.last_name
    
