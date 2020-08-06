from django.shortcuts import render

def home(request):
    return render(request,'shop/home.html')
def rate(request):
   return render(request,'shop/rate.html')
def services(request):
   return render(request,'shop/services.html')
def myaccount(request):
   return render(request,'shop/myaccount.html')
def buyform(request):
    return render(request,'shop/Buyform.html')
