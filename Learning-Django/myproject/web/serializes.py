

from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import *
from rest_framework.validators import UniqueTogetherValidator
class ProductSerialize(serializers.ModelSerializer):
    class Meta:
        model=Products
        fields=['id','productName','price','quantity','description','category']


class CategorySerialize(serializers.ModelSerializer):
    products = ProductSerialize(many=True,read_only=True)

    class Meta:
        model = Categories
        fields = ['id','categoryName','products']
        validators = [
            UniqueTogetherValidator(
                queryset=Categories.objects.all(),
                fields=['categoryName']
            )
        ]

class OrderDetailSerialize(serializers.ModelSerializer):
    class Meta:
        model=OrderDetails        
        fields=['id','product','quantity','price']


class OrderSerialize(serializers.ModelSerializer):
    # ordersDetail = OrderDetailSerialize(many=True)

    class Meta:
        model=Orders        
        fields=['id','recipientPhone','recipientName','note','isProcess','customer']
        depth = 2

    def create(self, validated_data):
        ordersDetail = validated_data.pop('ordersDetail')
        order = Orders.objects.create(**validated_data)
        for orderDetail in ordersDetail:
            OrderDetails.objects.create(order=order,**orderDetail)
        
        return order

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class UserSerialize(serializers.ModelSerializer):
        # orders = OrderSerialize(many=True)
    password2 = serializers.CharField(style={'input_type':'password'},write_only=True)
    class Meta:
        model=User
        fields=('id','password','email','username','last_name','password2')
    
    def create(self, validated_data):
        password = validated_data['password']
        password2 = validated_data['password2']
        if(password!=password2):
            raise serializers.ValidationError({'password':'password is not match'})
        else:
            del validated_data['password2']
            user = User.objects.create_user(**validated_data)
        
            token = Token.objects.create(user=user)
        # print({'user':user,'token':token})
            return user

class LogInUserSerialize(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('username','password')
    

    


