#this file is to help create user groups in the system who will be assigned different roles
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.models import BaseCommand

class Command(BaseCommand):
    help = 'Assign permissions tp user groups for the feedback system'
    #creating user groups allows one to manage different types of users

    #HAS CREATED MODEL-SPECIFIC PERMISSIONS
    #will import the permissions models so that it is linked to the user groups of the system
    def handle(self, *args, **kwargs):
        #creates groups for customers, the salon owner and stylists
        groups = ['Stylists', 'Salon Owner', 'Customer']
        for group in groups:
            Group.objects.get_or_create(name=group)
            #will create the group if it doesn't exist
        self.stdout.write(self.style.SUCCESS('Successfully created user groups created'))  
        #this will print a success message to the console
