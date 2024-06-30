from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser
from shortuuid.django_fields import ShortUUIDField


#Create your models here.

class User(AbstractUser):
    employee_id = ShortUUIDField(unique=True, length=5, max_length=10, prefix="emp", alphabet="abcdef12345")
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    phone = PhoneNumberField()
    profile_image = models.ImageField(default="fallback.png", upload_to="proflile-images", blank=True)

    USERNAME_FIELD = "last_name"
    REQUIRED_FIELDS = [
        'employee_id',
        'first_name',
        'phone',
    ]



    def __str__(self):
        return self.last_name +"   " + self.first_name


