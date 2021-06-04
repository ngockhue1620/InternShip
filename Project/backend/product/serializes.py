from rest_framework import serializers
from .models import Category,Product

from rest_framework.validators import UniqueTogetherValidator

class CategorySerialize(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id','categoryName']
        validators = [
            UniqueTogetherValidator(
                queryset=Category.objects.all(),
                fields=['categoryName']
            )
        ]

class ProductSerialize(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id','productName','price','quantity','description','category','image']
        