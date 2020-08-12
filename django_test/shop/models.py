from django.db import models

class Product(models.Model):
    id = models.AutoField
    Product_name = models.CharField(max_length=20,default="")
    Product_category = models.CharField(max_length=25,default="")
    Product_subcategory = models.CharField(max_length=20,default="")
    Product_description = models.CharField(max_length=500,default="")
    Product_price = models.IntegerField(default=0)
    Product_PubDate = models.DateField()
    Product_image = models.ImageField(upload_to="shop/images",default="")

    def __str__(self):
        return self.Product_name


