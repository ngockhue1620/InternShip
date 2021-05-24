
# from rest_framework.response import Response
# from django.http import HttpResponse,JsonResponse
# from rest_framework import status
# from rest_framework.parsers import JSONParser
# from django.views.decorators.csrf import csrf_exempt
# from .models import Article
# from  .serializers import ArticleSerilize
# from rest_framework.decorators import api_view
# from rest_framework.decorators import api_view

# @csrf_exempt
# def articles_list(request):
#     print("vao day")

#     if request.method == 'GET':
#         articles = Article.objects.all()
#         serialize = ArticleSerilize(articles,many=True)
#         return JsonResponse(serialize.data ,safe =False)
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serialize = ArticleSerilize(data=data)
#         if serialize.is_valid():
#             serialize.save()
#             return JsonResponse(serialize.data,status=201)
#         else:
#             return JsonResponse(serialize.errors,status=400)

# @csrf_exempt
# def article_detail(request,id):
#     'this funtion is show article detail'
#     'if method = get , return json data'

#     'if method = put , it means you must update data with key'
#     'first step you set a variable equal JSONParser.parse(request)'
#     'it means convert the data request from json'

#     try:
#         article = Article.objects.get(id=id)
#     except Article.DoesNotExist:
#         return HttpResponse(status=404)
    
#     if request.method == 'GET':
#         serializer = ArticleSerilize(article)
#         return JsonResponse(serializer.data)
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = ArticleSerilize(article,data=data)
#         if serializer.is_valid():           
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors,status=400)
#     elif request.method == 'DELETE':
#         article.delete()
#         return HttpResponse(status=204)

# @api_view(['GET','POST'])
# def articles_list(request,format=None):
    
#     if request.method == 'GET':
#         article = Article.objects.all()
#         serialzer = ArticleSerilize(article,many=True)
#         return Response(serialzer.data)
#     if request.method == "POST":
        
#         serializer = ArticleSerilize(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
# @api_view(['GET','PUT','DELETE'])
# def article_detail(request,id,format=None):

#     try:
#         # article= Article.objects.filter(id=id).get()
#         article= Article.objects.get(id=id)
#     except Article.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'GET':
#         serialize = ArticleSerilize(article)
#         return Response(serialize.data)
    
#     if request.method == 'PUT':
#         serialize = ArticleSerilize(article,data=request.data)
#         if serialize.is_valid():
#             serialize.save()
#             return Response(serialize.data)
#         return Response(status=status.HTTP_400_BAD_REQUEST)
#     if request.method == 'DELETE':
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#-------------class view
from rest_framework.serializers import Serializer
from .models import Article
from .serializers import ArticleSerilize
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from django.shortcuts import get_object_or_404

class ArticleViewSet(viewsets.ViewSet):

    def list(self, request):
        articles = Article.objects.all()
        serialize = ArticleSerilize(articles,many=True)
        return Response(serialize.data)

    def create(self, request):
        
        serializer = ArticleSerilize(data=request.data)

        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):

        article =get_object_or_404(Article,pk=pk)
        serialize = ArticleSerilize(article)
        return Response(serialize.data)

    def update(self, request, pk=None):
        article =Article.objects.get(pk=pk)
        serialize = ArticleSerilize(article,data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        return Response(serialize.errors,status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        atricle = Article.objects.get(pk=pk)
        atricle.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ArticleList(APIView):

    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    authentication_classes=[TokenAuthentication]
    permission_classes = [IsAuthenticated]

    # def get(self, request, format=None):
    #     content = {
    #         'user': str(request.user),  # `django.contrib.auth.User` instance.
    #         'auth': str(request.auth),  # None
    #     }
    #     return Response(content)   
    def get(self,request,format=None):
        article = Article.objects.all()
        serializer = ArticleSerilize(article,many=True)
        return Response(serializer.data)
    # def post(self,request,format=None):
    #     serialize = ArticleSerilize(data=request.data)
    #     if serialize.is_valid():
    #         serialize.save()
    #         return Response(serialize.data,status=status.HTTP_201_CREATED)
    #     return Response(serialize.errors,status=status.HTTP_400_BAD_REQUEST)

class ArticleDetail(APIView):

    def get_object(self,id):
        try:
            return Article.objects.get(id=id)
        except Article.DoesNotExist:
            raise Http404

    def get(self,request,id,format=None):
        article = self.get_object(id)
        serializer= ArticleSerilize(article)
        return Response(serializer.data)

    def put(self,request,id,format=None):
        article = self.get_object(id)

        serialaze =ArticleSerilize(article,data=request.data)
        if serialaze.is_valid():
            serialaze.save()
            return Response(serialaze.data)
        return Response(serialaze.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id,format=None):
        article = self.get_object(id)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# using mixins
# from .models import Article
# from .serializers import ArticleSerilize
# from rest_framework import mixins
# from rest_framework import generics

# class ArticalList(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
    
#     queryset =Article.objects.all()
#     serializer_class = ArticleSerilize

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
    
#     def post(self,requset, *args, **kwargs):
#         return self.create(requset,*args, **kwargs)

# class ArticleDetail(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):

#     queryset = Article.objects.all()

#     serializer_class = ArticleSerilize

#     def get(self,request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self,request,*args, **kwargs):
#         return self.update(request,*args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

# from .models import Article
# from .serializers import ArticleSerilize
# from rest_framework import generics


# class ArticalList(generics.ListCreateAPIView):
#     queryset=Article.objects.all()
#     serializer_class = ArticleSerilize
# class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset =Article.objects.all()
#     serializer_class =ArticleSerilize