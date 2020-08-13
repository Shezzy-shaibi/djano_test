from django.shortcuts import render
from .models import Product


def home(request):

    products = Product.objects.all()
    parms = {'product': products}
    return render(request,'shop/home.html',parms)
def rate(request):
   return render(request,'shop/rate.html')
def services(request):
   return render(request,'shop/services.html')
def myaccount(request):
   return render(request,'shop/myaccount.html')
def buyform(request):
    return render(request,'shop/Buyform.html')
