from django.urls import path
from employeeapp import views
from .views import RegisterStylist, CreateSalonOwner, UpdateStylist, LogoutStylist, DeleteStylist, StylistDetail, StylistRecord, LoginStylist, LoginSalonOwner


urlpatterns = [
    

    path('records', views.records, name="records"),

    #these are urls for the surveys
    path('salonowner/', CreateSalonOwner.as_view(), name='salonowner'),

    path('owner/login/', LoginSalonOwner.as_view(), name='login-owner'),

    path('register/', RegisterStylist.as_view(), name='register'),

    path('logout/', LogoutStylist.as_view(), name='logout'),

    path('login/', LoginStylist.as_view(), name='login'),

    path('stylist/edit/<int:pk>/', UpdateStylist.as_view(), name='update-stylist'),

    path('stylist/delete/<int:pk>/', DeleteStylist.as_view(), name='delete-stylist'),

    path('stylist/details/<int:pk>/', StylistDetail.as_view(), name='stylist-details'),

    path('stylist/list/', StylistRecord.as_view(), name='stylist-records'),


    

    
]