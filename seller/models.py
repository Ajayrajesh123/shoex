from django.db import models

class SellerRegestration(models.Model):
    fullname=models.TextField(max_length=100,null=True)
    email=models.TextField(max_length=100,null=True)
    password=models.TextField(max_length=100,null=True)
      
    def __str__(self):
         return self.fullname

 

class Category(models.Model):
    name=models.TextField(max_length=100,null=True)

    def __str__(self):
         return self.name
class Product(models.Model):
    product_name=models.TextField(max_length=100,null=True)
    description=models.TextField(max_length=100,null=True)
    price=models.FloatField(null=True)
    category_name=models.ForeignKey(Category,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='products',null=True)