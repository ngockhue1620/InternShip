from django.db import models
from django.shortcuts import reverse
class Categories(models.Model):
    categoryName    = models.CharField(max_length=200)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)
    def __str__(self):        
        return self.categoryName
    
    def get_absolute_url(self):
        return reverse("category_detail_url", kwargs={"categoryName": self.categoryName})
    

class Products(models.Model):
    productName     = models.CharField(max_length=255)
    price           = models.BigIntegerField()
    quantity        = models.IntegerField()
    img             = models.TextField()
    description     = models.TextField()
    category      = models.ForeignKey(Categories, on_delete=models.CASCADE)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)
    
    def __str__(self):        
        return self.id
    def get_absolute_url(self):
    
        return reverse("product_detail_url", kwargs={"id": self.id})
    
        
class Customers(models.Model):
    customerName    = models.CharField(max_length=100)
    customerEmail   = models.EmailField()
    password        = models.CharField(max_length=255)
    phone           = models.CharField(max_length=20)
    address         = models.CharField(max_length=255)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

    def __str__(self) :
        return self.customerEmail
    def get_absolute_url(self):
        return reverse("customer_detail_url", kwargs={"customerEmail": self.customerEmail})
    
    

class Orders(models.Model):
    Customer    = models.ForeignKey(Customers, on_delete=models.CASCADE)
    recipientPhone  = models.TextField(max_length=20)
    recipientName   = models.TextField(max_length=100)
    note            = models.TextField(max_length=200,blank=True)
    isProcess       = models.BooleanField()
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)
class OrderDetails(models.Model):
    order        = models.ForeignKey(Orders,on_delete=models.CASCADE)
    product      = models.ForeignKey(Products,on_delete=models.CASCADE)
    quantity        = models.IntegerField()
    price           = models.BigIntegerField()
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)
class InCarts(models.Model):
    customer    = models.ForeignKey(Customers,on_delete=models.CASCADE)
    product      = models.ForeignKey(Products,on_delete=models.CASCADE)
