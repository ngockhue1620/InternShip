from django.core.exceptions import ValidationError
from rest_framework import serializers
from .models import Order, OrderDetail

class OrderDetailSerialize(serializers.ModelSerializer):

    class Meta:
        model = OrderDetail
        fields = ['id','product','price','quantity']

class OrderSerialize(serializers.ModelSerializer):
    orders_detail = OrderDetailSerialize(many=True)
    class Meta:
        model = Order
        fields = ['id','resipientName','resipientPhone','resipientAddress','orders_detail','user','note']
    

    def create(self, validated_data):
        orders_detail = validated_data.pop('orders_detail')
        order = Order.objects.create(**validated_data)
        for orderDetail in orders_detail:
            
            OrderDetail.objects.create(order=order,**orderDetail)
            
        
        return order

from django.contrib.auth.models import User       

class UserSerialize(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username','password']
