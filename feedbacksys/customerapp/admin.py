from django.contrib import admin
from .models import Customer

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number', 'date_joined',)
    #affect what will be displayed in the database for customers

# Register your models here.
admin.site.register(Customer, CustomerAdmin)
