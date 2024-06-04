from django.urls import path
from feedbackapp import views

urlpatterns = [
    path('', views.index, name="index"),

    path('dashboard', views.dashboard, name="dashboard"),

    path('employee-profile', views.employee_profile, name="employee-profile"),
]