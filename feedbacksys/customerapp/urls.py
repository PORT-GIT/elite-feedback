from django.urls import path
from customerapp import views

urlpatterns= [
    path('', views.customer, name="customer"),

    path('profile', views.profile, name="profile"),
]