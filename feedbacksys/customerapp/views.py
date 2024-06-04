from django.shortcuts import render

# Create your views here.
def add_customer(request):

    return render(request, 'customerapp/add-customer.html')

def customer_profile(request):

    return render(request, 'customerapp/customer-profile.html')

def customer_records(request):
    
    return render(request, 'customerapp/customer-records.html')