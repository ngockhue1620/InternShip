
from rest_framework.views import APIView
from .serializes import OrderSerialize, UserSerialize
from .models import Order

from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ViewSet

from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
class OrderViewSet(ViewSet):
    queryset = Order.objects.all()
    def list(self, request):

             
        seralize = OrderSerialize(self.queryset,many=True)    
        return Response(seralize.data)

        

    def create(self, request):
        serialize = OrderSerialize(data=request.data)

        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data,status=status.HTTP_201_CREATED)
    
    def retrieve(self, request, pk=None):
        
        order = get_object_or_404(self.queryset,user=pk)
        serialize = OrderSerialize(order)
        return Response(serialize.data)
from django.contrib.auth import authenticate

class LoginViewSet(APIView):

    def post(self, request, format=None):
        print("in",request.data)
        serialize = UserSerialize(data=request.data)
        
        if serialize.is_valid():
            print("2",serialize.data['password'])
            name = serialize.data['username']
            password = serialize.data['password']
            userlogin = authenticate(username=name, password=password)
            print(userlogin)
            if userlogin is not None:
                print(userlogin)
                return Response(

                   {"isAuthen":"Ok"} 
                )
            else:
                return Response({"isAuthen":False})
    