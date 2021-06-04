from django.urls.conf import include
from .views import LoginViewSet, OrderViewSet
from django.urls import path
from rest_framework.routers import DefaultRouter

route = DefaultRouter()
route.register('order',OrderViewSet,basename='order')

urlpatterns = [
   
   path('api/',include(route.urls)),
   
  
   
]
