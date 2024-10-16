from django.db import models
from location_field.models.plain import PlainLocationField
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

#i have re-written the custom user model provided by django so that it will fit the requirements of the system
#in that i have three different users of the system


#creating models for the salon registration
class Salon(models.Model):
    name = models.CharField(max_length=100, blank=False)
    location = PlainLocationField(based_fields=['city'], zoom=7)
    phone_number = PhoneNumberField(blank=False) 

    def __str__(self):
        return self.name
    
class SalonManager(BaseUserManager):
    #this class will be used to contain methods to be applied by the SalonOwner class below
    #will create typical user and superuser

    def create_user(self, first_name, last_name, email, phone_number, password=None):
        if not email:
            raise ValueError("Email must be provided")

        if not phone_number:
            raise ValueError("Phone number must be provided")
        
        user=self.model(
            email=self.normalize_email(email),
            #it will take the email uppercase letters and convert to lowercase letters
            phone_number=phone_number,
            first_name=first_name,
            last_name=last_name
        )

        user.set_password(password)
        #this is a method that will encode any password provided by user into the database
        user.save(using=self._db)
        #this is defining which database the BaseUserManager should use
        return user

    
    

#creating models for owner of the salon and stylist of salon using abstractuser
class SalonOwner(AbstractBaseUser):
    name = models.CharField(max_length=100, blank=False)



