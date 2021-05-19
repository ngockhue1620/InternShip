
from django.urls import path
from .views import CreateCategory, CreateCustomer,category_list,CategoryDetail,CreateProduct,ProductDetail,products_list,CustomerDetail

urlpatterns = [
    
    path('category/create',CreateCategory.as_view(),name='category_create_url'),
    path('categories/list',category_list,name='categories_list_url'),
    path('category/<str:categoryName>',CategoryDetail.as_view(),name="category_detail_url"),

    path('product/create',CreateProduct.as_view(),name='product_create_url'),
    path('product/<int:id>',ProductDetail.as_view(),name="product_detail_url"),
    path('products/list',products_list,name="products_list_url"),

    path('customer/create',CreateCustomer.as_view(),name='customer_create_url'),
    path('customer/<str:customerEmail>',CustomerDetail.as_view(),name='customer_detail_url')
]