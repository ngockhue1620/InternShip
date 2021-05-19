

from django.shortcuts import redirect, render ,get_list_or_404

from django.views.generic import View

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
 
