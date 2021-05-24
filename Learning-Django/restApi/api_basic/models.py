from django.db import models


class Article(models.Model):
    titie = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    date  = models.DateTimeField(auto_now_add =True)

    def __Str__(self):
        return self.title


