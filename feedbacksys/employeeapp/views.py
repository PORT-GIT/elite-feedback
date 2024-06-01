from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def employee_profile(request):

    return HttpResponse ("Hello!")

def login(request):

    return HttpResponse ("Login!")

def records(request):

    return HttpResponse ("Hello!")

def register(request):

    return HttpResponse ("Hello!")
