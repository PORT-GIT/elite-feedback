from django.shortcuts import render

# Create your views here.
def customer(request):

    return render(request, 'customerapp/add-customer.html')

def profile(request):
    return render(request, 'customerapp/customer-profile.html')