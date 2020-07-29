
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('rate', views.rate, name="rate"),
    path('services', views.services, name="services"),
    path('myaccount', views.myaccount, name="myaccount")
    ]
