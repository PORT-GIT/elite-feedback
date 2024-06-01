from django.urls import path
from feedbackapp import views

urlpatterns = [
    path('', views.home, name="home"),

    path('loginpage', views.loginpage, name="loginpage"),
]