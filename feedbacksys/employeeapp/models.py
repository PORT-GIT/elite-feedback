# from django.db import models
# from location_field.models.plain import PlainLocationField
# from phonenumber_field.modelfields import PhoneNumberField
# from .validators import phonenumber_validation
# #imports the validation code from the validation file

    
# class SystemUsers(models.Model):
#     #these are the choices for the role
#     ROLE_CHOICES = (
#         ('SALON OWNER', 'Salon Owner'),
#         ('STYLIST', 'Stylist'),

#     )
#     first_name = models.CharField(max_length=100, blank=False)
#     last_name = models.CharField(max_length=100, blank=False)
#     email = models.EmailField(max_length=100, blank=False, unique=True)
#     phone_number = PhoneNumberField(region='KE', blank=False, unique=True, validators=[phonenumber_validation])
#     #extending the phonenumber django library will allow me to put regulation on the phonenumbers entered
#     #like the length and the code of the number
#     role = models.CharField(choices=ROLE_CHOICES, blank=False, null=False)
#     date_joined = models.DateField(auto_now=True, blank=False, null=False)

#     def __str__ (self):
#         return f'{self.first_name} {self.last_name}'

    
    



