from django.urls import path
from employeeapp import views

urlpatterns = [
    
    path('register', views.register, name="register"),

    path('login', views.login, name="login"),

    path('records', views.records, name="records"),

    
]