from re import T
from django.db.models.base import Model
from rest_framework import serializers
from .models import *

class ProductSerialize(serializers.ModelSerializer):
    class Meta:
        model=Products
        fields=['id','productName','price','quantity','description','category']


class CategorySerialize(serializers.ModelSerializer):
    products = ProductSerialize(many=True,read_only=True)

    class Meta:
        model = Categories
        fields = ['id','categoryName','products']


class OrderDetailSerialize(serializers.ModelSerializer):
    class Meta:
        model=OrderDetails        
        fields=['id','product','quantity','price']


class OrderSerialize(serializers.ModelSerializer):
    ordersDetail = OrderDetailSerialize(many=True)

    class Meta:
        model=Orders        
        fields=['id','recipientPhone','recipientName','note','isProcess','customer','ordersDetail']

    def create(self, validated_data):
        ordersDetail = validated_data.pop('ordersDetail')
        order = Orders.objects.create(**validated_data)
        for orderDetail in ordersDetail:
            OrderDetails.objects.create(order=order,**orderDetail)
        
        return order


class CustomerSerialize(serializers.ModelSerializer):
    orders = OrderSerialize(many=True,read_only=True)

    class Meta:
        model=Customers
        fields=['id','customerName','customerEmail','password','phone','address','orders']

