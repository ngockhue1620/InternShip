
from django.db import router
from django.urls import path
from .views import *
from django.urls.conf import include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('category',CategoryViewSet,'category')
router.register('product',ProductViewSet,'product')
router.register('customer',CustomerViewSet,'customer')
router.register('order',OrderViewSet,'order')

urlpatterns = [
    
    path('category/create',CreateCategory.as_view(),name='category_create_url'),
    path('categories/list',category_list,name='categories_list_url'),
    path('category/<str:categoryName>',CategoryDetail.as_view(),name="category_detail_url"),

    path('product/create',CreateProduct.as_view(),name='product_create_url'),
    path('product/<int:id>',ProductDetail.as_view(),name="product_detail_url"),
    path('products/list',products_list,name="products_list_url"),

    path('customer/create',CreateCustomer.as_view(),name='customer_create_url'),
    path('customer/<str:customerEmail>',CustomerDetail.as_view(),name='customer_detail_url'),

    path('api/',include(router.urls)),
    path('login',LoginUserViewSet.as_view())
]