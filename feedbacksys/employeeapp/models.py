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
    password = models.CharField(max_length=50, blank=False)
    
    def __str__ (self):
        return f'{self.first_name} {self.last_name}'
    
    class Meta:
        permissions = [
            ("can_view_survey", "Can view survey"),
            ("can_edit_survey", "Can edit survey"),
            ("can_delete_survey", "Can delete survey"),
            ("can_send_survey","Can send survey"),
            ("can_create_survey", "Can create survey"),
            ("can_create_question", "Can create question"),
            ("can_view_question", "Can view question"),
            ("can_edit_question", "Can edit question"),
            ("can_delete_question", "Can delete question"),
            ("can_create_customer","Can create customer"),
            ("can_view_customer","Can view customer"),
            ("can_edit_customer","Can edit customer"),
            ("can_delete_customer","Can delete customer"),
            ("can_create_stylist","Can create stylist"),
            ("can_view_stylist","Can view stylist"),
            ("can_edit_stylist","Can edit stylist"),
            ("can_delete_stylist","Can delete stylist"),
            ("can_respond_to_survey_response", "Can respond to survey response"),
            ("can_view_survey_response", "Can view survey response"),
            ("can_delete_survey_response", "Can delete survey response"),
        ]
    

class Stylist(models.Model):
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=100, blank=False, unique=True)
    phone_number = PhoneNumberField(region='KE', blank=False, unique=True, validators=[phonenumber_validation])
    #extending the phonenumber django library will allow me to put regulation on the phonenumbers
    #entered like the length and the code of the number
    password = models.CharField(max_length=50, blank=False)

    def __str__ (self):
        return f'{self.first_name} {self.last_name}'
    
    class Meta:
        permissions = [
            ("can_view_survey", "Can view survey"),
            ("can_edit_survey", "Can edit survey"),
            ("can_send_survey","Can send survey"),
            ("can_create_survey", "Can create survey"),
            ("can_create_question", "Can create question"),
            ("can_view_question", "Can view question"),
            ("can_edit_question", "Can edit question"),
            ("can_delete_question", "Can delete question"),
            ("can_create_customer","Can create customer"),
            ("can_view_customer","Can view customer"),
            ("can_edit_customer","Can edit customer"),
            ("can_view_stylist","Can view stylist"),
            ("can_edit_stylist","Can edit stylist"),
            ("can_respond_to_survey_response", "Can respond to survey response"),
            ("can_view_survey_response", "Can view survey response"),
        ]
    


    
    
    



