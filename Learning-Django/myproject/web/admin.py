from django.contrib import admin

# Register your models here.
from .models import  *
admin.site.register(Categories)
admin.site.register(Products)
admin.site.register(Customers)
admin.site.register(Orders)
