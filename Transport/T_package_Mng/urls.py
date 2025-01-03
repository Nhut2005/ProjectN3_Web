from django.urls import path
from . import views

urlpatterns = [
    path('T_package_Mng/', views.Order, name='T_package_Mng'),
    path('T_package_Mng/', views.Employee, name='T_package_Mng'),
    path('T_package_Mng/', views.Customer, name='T_package_Mng'),
]