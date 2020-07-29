from django.shortcuts import render

def home(request):
    return render(request,'shop/home.html')
def rate(request):
   return render(request,'rate.html')
def services(request):
   return render(request,'services.html')
def myaccount(request):
   return render(request,'myaccount.html')
