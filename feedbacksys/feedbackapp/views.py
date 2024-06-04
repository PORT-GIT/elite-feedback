from django.shortcuts import render


# Create your views here.

def index(request):
    
    return render(request, 'feedbackapp/index.html')

def dashboard(request):

    return render( request, 'feedbackapp/dashboard.html')

def employee_profile(request):

    return render (request, 'feedbackapp/employee-profile.html')