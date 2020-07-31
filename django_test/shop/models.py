from django.db import models

class form(models.Model):
    id = models.AutoField
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20,default='')
    email = models.CharField(max_length=25)
    password = models.CharField(max_length=16)
    Address = models.CharField(max_length=50)
    Address2 = models.CharField(max_length=50,default='')
    city = models.CharField(max_length=15)
    state = models.CharField(max_length=25)
    zip = models.CharField(max_length=15)


