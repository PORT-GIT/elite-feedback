from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from .models import Stylist, SalonOwner
from .forms import StylistRegistrationForm, StylistLoginForm, SalonOwnerRegistrationForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
# Create your views here.


def records(request):

    return render (request, 'employeeapp/records.html')


class CreateSalonOwner(CreateView):
    pass

class LoginSalonOwner(LoginView):
    pass

class LogoutSalonOwner(LogoutView):
    pass

class RegisterStylist(CreateView):
    model = Stylist
    form_class = StylistRegistrationForm
    template_name = 'employeeapp/register.html'
    success_url = reverse_lazy('login')

    def form_valid (self, form):
        messages.sucess(self.request, "Customer registered successfully!")
        return super().form_valid(form)
    
class LoginStylist(LoginView):
    form_class = StylistLoginForm
    template_name = 'employeeapp/login.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):

        #this below is used to retrieve form data
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        password = form.cleaned_data['password']
        confirm_password = form.cleaned_data['confirm_password']
        #cleaned_data is a dictionary that contains validated data from the form
        #so once the form data is validated the cleaned_data is populated in the database

        try:
            stylist = Stylist.objects.get(self.request, first_name=first_name, last_name=last_name, password=password, confirm_password=confirm_password)
        except Stylist.DoesNotExist:
            return render(self.request, 'employeeapp/login.html', {'error': 'Invalid credentials'})
        
        if stylist is not None:
            if stylist.check_password(password):
                login(self.request, stylist)
                messages.success(self.request, 'Stylist is logged in!')
                return redirect(self.success_url)
            
        form.add_error(None, "Invalid login credentials")
        return self.form_invalid(form)


class LogoutStylist(LogoutView):
    pass
    
class UpdateStylist(UpdateView, LoginRequiredMixin):
    pass

class DeleteStylist(DeleteView, LoginRequiredMixin):
    pass

class StylistDetail(DetailView, LoginRequiredMixin):
    template_name = 'employeeapp/stylist-details.html'
    pass

class StylistRecord(ListView, LoginRequiredMixin):
    template_name = 'employeeapp/stylist-records.html'
    pass

