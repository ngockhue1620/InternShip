from rest_framework import serializers
from .models import Article

# class ArticleSerialize(serializers.Serializer):
#     titie = serializers.CharField(max_length=200)
#     author = serializers.CharField(max_length=200)
#     email = serializers.EmailField(max_length=100)
#     date  = serializers.DateTimeField()

#     def create(self, validated_data):
#         return Article.objects.create(validated_data)
    
#     def update(self, instance, validated_data):
       
#        instance.titie = validated_data.get('title',instance.titie)
#        instance.author = validated_data.get('author',instance.author)
#        instance.email = validated_data.get('email',instance.email)
#        instance.dtae = validated_data.get('date',instance.date)
#        instance.save()
#        return instance
class ArticleSerilize(serializers.ModelSerializer):
    class  Meta:
        model = Article
        fields=['id','titie','author','email']