from django.db import models
from location_field.models.plain import PlainLocationField
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser


#creating models for the salon registration
class Salon(models.Model):
    name = models.CharField(max_length=100, blank=False)
    location = PlainLocationField(based_fields=['city'], zoom=7)
    phone_number = PhoneNumberField(blank=False) 

    def __str__(self):
        return self.name
    

#creating models for owner/admin of salon registration
class SalonOwner(models.Model):
    name = models.CharField(max_length=100, blank=False)




#creating model for stylists registration
class Stylist(models.Model):
    name = models.CharField(max_length=100, blank=False)
    