from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from .models import Customer
from .forms import CustomerRegistrationForm
from django.contrib import messages

# Create your views here.
def add_customer(request):

    return render(request, 'customerapp/add-customer.html')

def customer_profile(request):

    return render(request, 'customerapp/customer-profile.html')

def customer_records(request):
    
    return render(request, 'customerapp/customer-records.html')

class RegisterCustomer(CreateView):
    model = Customer
    form_class = CustomerRegistrationForm
    template_name = 'customerapp/add-customer.html'
    success_url = reverse_lazy('customer-records')

    def form_valid (self, form):
        messages.sucess(self.request, "Customer registered successfully!")
        return super().form_valid(form)
    


class CustomerRecords(ListView):
    pass

class CustomerDetails(DetailView):
    pass

class UpdateCustomer(UpdateView):
    pass