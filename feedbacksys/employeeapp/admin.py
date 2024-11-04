from django.contrib import admin
from .models import SalonOwner, Stylist

# Register your models here.

admin.site.register(SalonOwner)
admin.site.register(Stylist)  # Registering Stylist model