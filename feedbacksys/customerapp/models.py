from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    phone_number = PhoneNumberField(blank=True)
    email = models.EmailField(max_length=50)
    date_joined = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.first_name +"   " + self.last_name