from django.urls import path
from customerapp import views

urlpatterns= [
    path('', views.add_customer, name="add_customer"),

    path('customer-profile', views.customer_profile, name="customer-profile"),

    path('customer-records', views.customer_records, name="customer-records"),
]