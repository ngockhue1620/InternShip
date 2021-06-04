from django.db import models


class Category(models.Model):

    categoryName = models.CharField(max_length=200)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

    def  __str__(self):
        return self.categoryName
    
class Product(models.Model):
    productName = models.CharField(max_length=200)
    price = models.BigIntegerField()
    quantity = models.IntegerField()
    description = models.TextField()
    image = models.TextField()
    category = models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.productName