

from re import S
from django.shortcuts import redirect, render ,get_list_or_404

from django.views.generic import View
from rest_framework.response import Response
from rest_framework.views import APIView

from .forms import CategoryForm,ProductForm,CustomerForm
from .models import Categories, Customers, Products


def category_list(request):
    
    result = Categories.objects.select_related().all()
    print(result)
    return render(request,'web/categories_list.html',context={'categories':result})

def products_list(request):
    products = Products.objects.all()
    return render(request,'web/products_list.html',context={'products':products})
    
class CreateCategory(View):

    def get(self,request):
        form = CategoryForm()
        return render(request,'web/create_category.html',context={'form':form})
        
    def post(self,request):
        bound_form = CategoryForm(request.POST)
        if bound_form.is_valid():
            new_category = bound_form.save()
            return redirect(new_category)
        return render(request,'web/create_category.html',context={'form':bound_form})

class CreateProduct(View):
    
    def get(self,request):
        
        form = ProductForm()
        return render(request,'web/create_product.html',context={'form':form})
    def post(self,request):

        bound_form = ProductForm(request.POST)
        if(bound_form.is_valid()):
            new_product = bound_form.save()    
            print("day ne",new_product.id)
                   
            return redirect(new_product)

        return render(request,'web/create_product.html',context={'form':bound_form})
   
class CreateCustomer(View):

    def get(self,request):
        form = CustomerForm()
        return render(request,'web/create_customer.html',context={'form':form})
    
    def post(self,request):

        bound_form = CustomerForm(request.POST)
        if bound_form.is_valid():
            new_customer=bound_form.save()
            return redirect(new_customer)
        return render(request,'web/create_customer.html',context={'form':bound_form})

class CategoryDetail(View):
    def get(self,request,categoryName):
        category = get_list_or_404(Categories,categoryName__iexact=categoryName)
        print(category)
        return render(request,'web/category_detail.html',context={'category':category})

class ProductDetail(View):
    def get(self,request,id):
        product = get_list_or_404(Products,id__iexact=id)
        return render(request,'web/product_detail.html',context={'product':product})
        
class CustomerDetail(View):

    def get(self,request,customerEmail):
        customer = get_list_or_404(Customers,customerEmail__iexact=customerEmail)
        return render(request,'web/customer_detail.html',context={'customer':customer})

from rest_framework import status, viewsets
from .serializes import *
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class CategoryViewSet(viewsets.ViewSet):

    authentication_classes=[TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def list(self,request):

        categories = Categories.objects.select_related().all()
        serialize  = CategorySerialize(categories,many=True)
        return Response(serialize.data)
    
    def create(self,request):
        serialize = CategorySerialize(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data,status=status.HTTP_201_CREATED)
        return Response(serialize.errors)


class ProductViewSet(viewsets.ViewSet):

    def list(self,request):

        products = Products.objects.all()
        serialize  = ProductSerialize(products,many=True)
        return Response(serialize.data)

    def create(self,request):
        serialize = ProductSerialize(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data,status=status.HTTP_201_CREATED)
        return Response(serialize.errors)
from django.db.models import Subquery

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
class CustomerViewSet(viewsets.ViewSet):

    def list(self,request):
        
        users = User.objects.all()        
        # UserParent.objects.filter(user_id__in=Subquery(users.values('id')))
        serialize  = UserSerialize(users,many=True)
        return Response(serialize.data)

    def create(self,request):
        serialize = UserSerialize(data=request.data)
        print("chay vo day roi")
        
        if serialize.is_valid():
            serialize.save()             
            # token = Token.objects.get(user=serialize.data['id'])
            # token = Token.objects.create(user=serialize.data)
            # print(serialize.data['username'])
            
            
            print(serialize.data)
            return Response(serialize.data,status=status.HTTP_201_CREATED)
           
        return Response(serialize.errors)
        
 

class OrderViewSet(viewsets.ViewSet):

    def list(self,request):
        products = Orders.objects.all()
        serialize  = OrderSerialize(products,many=True)
        return Response(serialize.data)

    def create(self,request):
        serialize = OrderSerialize(data = request.data)
        
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data,status=status.HTTP_201_CREATED)
        return Response(serialize.errors)

from django.contrib.auth import authenticate, login

class LoginUserViewSet(APIView):
    def get(self, request, format=None):
        users = User.objects.all()        
        # UserParent.objects.filter(user_id__in=Subquery(users.values('id')))
        serialize  = LogInUserSerialize(users,many=True)
        return Response(serialize.data)
    def post(self, request, format=None):
        print(request.data)
        serialize = LogInUserSerialize(data=request.data) 
         
        if serialize.is_valid():
            username = serialize['username']
            password = serialize['password']
            print(username,password)
            userlogin = authenticate(request, username=username, password=password)
            if userlogin is not None:
                login(request, userlogin)
                token = Token.objects.get(user=username)
                return Response(token,status=status.HTTP_200_OK)
        return Response({'error':'password or userName is wrong'},status=status.HTTP_400_BAD_REQUEST)
