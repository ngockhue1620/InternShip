from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
def index(request):
    animals=['zebra','cart','dog']
    return render(request,'blogdjango/index.html',context={'animals':animals})
