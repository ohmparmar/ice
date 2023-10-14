from django.contrib import admin
from django.urls import path
from project import views
urlpatterns = [
    path("",views.landing,name='landing'),
    path("login",views.loginuser,name='login'),
    path("dashboard",views.dashboard,name='dashboard'),
    path("logout",views.logoutuser,name='logout'),
    path("purchase",views.purchase,name='purchase'),
    path("stocks",views.stocks,name='stocks'),
    path("sales",views.sales,name='sales'),
    
]   
