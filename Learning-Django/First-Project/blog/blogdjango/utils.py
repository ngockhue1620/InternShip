from django.shortcuts import redirect, render
from .models import *
from django.shortcuts import get_object_or_404



class  DetailObjectMinxin:

    model = None
    template=None 
    def get(self, request, slug):
        print("slug ne",slug)
        # post= self.model.objects.get(slug__iexact=slug)
        obj=get_object_or_404(self.model,slug__iexact=slug)
        
        return render(request,self.template,context={self.model.__name__.lower(): obj,'admin_object' : obj})

class CreateObjectMixin:
    modelForm = None
    template = None

    #get funtion is render form to create 
    def get(self,request):       
        form = self.modelForm
        return render(request,self.template,context={'form':form})
    #post function to save
    def post(self,request):  
        bound_from = self.modelForm(request.POST)  
        if(bound_from.is_valid()):            
            new_obj = bound_from.save()   
            return redirect(new_obj)
        return render(request,self.template,context={'form':bound_from})

class UpdateObjectMixin:
    model = None
    template  = None
    form_class = None

    def get(self,request,slug):
        obj = get_object_or_404(self.model,slug__iexact=slug)
        bound_form = self.form_class(instance=obj)
        return render(request,self.template,context={'form':bound_form, self.model.__name__.lower():obj})
    
    def post(self,request,slug):

        obj = get_object_or_404(self.model,slug__iexact=slug)

        bound_form = self.form_class(request.POST, instance=obj)

        if(bound_form.is_valid()):
            new_obj = bound_form.save()
            return redirect(new_obj)

        return render(request,self.template,context={'form':bound_form, self.model.__name__.lower():obj})

class DeleteObjectMixin:
    model =None
    template =None
    redirect_url = None

    def get(self,request,slug):

        obj = get_object_or_404(self.model,slug__iexact=slug)

        return render(request,self.template,context={self.model.__name__.lower():obj } ) 
    
    def post(self,request,slug):

        obj = get_object_or_404(self.model,slug__iexact=slug)
        obj.delete()

        return redirect(reverse(self.redirect_url))
