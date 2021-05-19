from django import forms
from .models import Categories,Products,Customers
from django.core.exceptions import ValidationError 

class CategoryForm(forms.ModelForm):
    class Meta:
        model=Categories
        fields = ['categoryName']
        widgets={
            'categoryName':forms.TextInput(attrs={'class':'form-control'})
        }

    def clean_categoryName(self):
        categoryName = self.cleaned_data.get('categoryName').lower()
        if Categories.objects.filter(categoryName__iexact=categoryName):
           raise ValidationError('Category Name should be UNIQUE. We have "{categoryName}" already')
        return categoryName

class ProductForm(forms.ModelForm):

    class Meta:
        model=Products
        fields= ['productName','price','quantity','description','img','category']
        widgets ={
            'productName':forms.TextInput(attrs={'class':'form-control'}),
            'price':forms.TextInput(attrs={'class':'form-control'}),
            'quantity':forms.TextInput(attrs={'class':'form-control'}),
            'img':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.TextInput(attrs={'class':'form-control'}),            
            'category':forms.Select(attrs={'class':'form-control'}),    
        }  

class CustomerForm(forms.ModelForm):
    class Meta:
        model=Customers
        fields=['customerName','customerEmail','password','phone','address']
        widgets ={
            'customerName':forms.TextInput(attrs={'class':'form-control'}),
            'customerEmail':forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'}),
            'phone':forms.TextInput(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'}),   
        }
    def clean_customerEmail(self):
        email = self.cleaned_data["customerEmail"]
        if Customers.objects.filter(customerEmail__iexact=email):
            raise ValidationError('"{email}" is already')
        return email
    
    def clean_phone(self):
        phone = self.cleaned_data["phone"]
        if Customers.objects.filter(phone__iexact=phone):
            raise ValidationError('"{phone}" is already')
        return phone
    
    def clean_password(self):
        password = self.cleaned_data["password"]
        if len(password)<8:
            raise ValidationError(' password must more than 8 word')
        return password
    
                
    


            
        
    