from django.urls import path
from django.urls.conf import include
from .views import CategoryList,ProductList,CategoryViewSet,ProductViewSet
from rest_framework.routers import DefaultRouter, Route

route = DefaultRouter()
route.register('category',CategoryViewSet,basename='category')
route.register('product',ProductViewSet,basename='product')
urlpatterns = [
    path('categorylist',CategoryList.as_view()),
    path('productlist',ProductList.as_view()),
    path('api/',include(route.urls))
]
