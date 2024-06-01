from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("welcome cutomer!")

def page(request):
    return HttpResponse("go login now!")