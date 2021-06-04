from django.shortcuts import render
from rest_framework import views
from rest_framework import viewsets
from rest_framework.views import APIView
from .serializes import CategorySerialize,ProductSerialize
from .models import Category,Product
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ViewSet


class CategoryList(APIView):

    def get(self,request,format=None):
        categories = Category.objects.all()
        serialize = CategorySerialize(categories,many=True)
        return Response(serialize.data)

class ProductList(APIView):

    def get(self,request,format=None):
        product = Product.objects.all()
        serializer = ProductSerialize(product,many=True)
        return Response(serializer.data)


class CategoryViewSet(viewsets.ViewSet):

    def list(self, request):
        categories = Category.objects.all()
        serialize = CategorySerialize(categories,many=True)
        return Response(serialize.data)

    def create(self, request):
        serialize = CategorySerialize(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data,status=status.HTTP_201_CREATED)
        return Response(serialize.errors,status.HTTP_400_BAD_REQUEST)

class ProductViewSet(viewsets.ViewSet):

    def list(self, request):       
        product = Product.objects.all()
        serializer = ProductSerialize(product,many=True)
        return Response(serializer.data)

    def create(self, request):
        serialize = ProductSerialize(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data,status=status.HTTP_201_CREATED)
        return Response(serialize.errors,status.HTTP_400_BAD_REQUEST)
