# from django.db import models
# from phonenumber_field.modelfields import PhoneNumberField
# from django.contrib.auth.models import AbstractUser
# #linking models from customerapp
# #from ..customerapp.models import customer

# #Create your models here.

# class User(AbstractUser):
#     employee_id = models.IntegerField(primary_key=True, on_delete=models.CASCADEA)
#     first_name = models.CharField(max_length=10)
#     last_name = models.CharField(max_length=10)
#     phone = PhoneNumberField()
#     profile_image = models.ImageField(default="fallback.png", upload_to="proflile-images", blank=True)

#     USERNAME_FIELD = "last_name"
#     REQUIRED_FIELDS = [
#         'employee_id',
#         'first_name',
#         'phone',
#     ]

#     def __str__(self):
#         return self.last_name +"   " + self.first_name


