from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def customer(request):
    return HttpResponse("welcome cutomer!")

def profile(request):
    return HttpResponse("go login now!")