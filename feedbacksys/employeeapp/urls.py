from django.urls import path
from employeeapp import views

urlpatterns = [
    path('', views.employee_profile, name="employee-profile"),
    
    path('register', views.register, name="register"),

    path('login', views.login, name="login"),

    path('records', views.records, name="records"),

    
]