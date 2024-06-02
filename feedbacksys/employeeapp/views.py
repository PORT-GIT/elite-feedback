from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def employee_profile(request):

    return render (request, 'employeeapp/employee-profile.html')

def login(request):

    return render (request, 'employeeapp/login.html')

def records(request):

    return render (request, 'employeeapp/records.html')

def register(request):

    return render (request, 'employeeapp/register.html')
