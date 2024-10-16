from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=10, blank=False)
    last_name = models.CharField(max_length=10, blank=False)
    phone_number = PhoneNumberField(blank=False)
    email = models.EmailField(max_length=50, null=True)
    date_joined = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.first_name +"   " + self.last_name
    

    #can use abstractbase user where i define each customer by their phonenumber
    #AbstractBaseUser  when you need a completely new user model with custom fields (like phone number as the primary identifier).
    #AbstractBaseUser is a base class that you can use to create your own custom user model
    #Use BaseUser Manager to manage how users are created, especially if you are using AbstractBaseUser