from django.db import models
from django.contrib.auth.models import User
from product.models import Product
# Create your models here.
class Order(models.Model):
    resipientName = models.CharField(max_length=100)
    resipientPhone = models.CharField(max_length=20)
    resipientAddress = models.CharField(max_length=255)
    note = models.CharField(blank=True,max_length=255)
    user = models.ForeignKey(User,related_name='orders',on_delete=models.CASCADE)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.resipientName

class OrderDetail(models.Model):
    price = models.BigIntegerField()
    quantity = models.IntegerField()
    product = models.ForeignKey(Product,related_name='product',on_delete=models.CASCADE)
    order = models.ForeignKey(Order,related_name='orders_detail',on_delete=models.CASCADE)

