from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=10, blank=False)
    last_name = models.CharField(max_length=10, blank=False)
    phone_number = PhoneNumberField(blank=False, unique=True)
    email = models.EmailField(max_length=50, null=True)
    date_joined = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.first_name +"   " + self.last_name
    
