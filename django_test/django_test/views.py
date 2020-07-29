# I have created this file
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
   return render(request,'homepage.html')
def rate(request):
   return render(request,'Rate.html')
def services(request):
   return render(request,'services.html')
def myaccount(request):
   return render(request,'myaccount.html')
def form(request):
   return render(request,'form.html')
def submit(request):
   return render(request,'form-submit.html')