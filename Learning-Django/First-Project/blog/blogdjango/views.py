from django.shortcuts import redirect, render
from django.shortcuts import redirect
from django.shortcuts import reverse
from django.views.generic import View
from django.shortcuts import get_object_or_404
from .models import Post,Tag
from .utils import DetailObjectMinxin,CreateObjectMixin,UpdateObjectMixin,DeleteObjectMixin
from django.db.models import Q
from .forms import TagForm,PostForm
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator

def post_list(request):
    seach_query = request.POST.get('seach','')
    if seach_query:
        posts=Post.objects.filter( Q(title__icontains=seach_query)|
       Q(body__icontains=seach_query)
       )
    else:
        posts = Post.objects.all()
    paginator =Paginator(posts,4)
    page_number = request.GET.get('page',1)
    page =paginator.get_page(page_number)

    seach_quuery = request.GET.get('seach','')
   

    if(page.has_next()):
        next_url =f'?page={page.next_page_number()}'
    else:
        next_url = ''
    
    if page.has_previous():
        prev = f'?page={page.previous_page_number()}'
    else:
        prev = ''

    return render(request,'./blogdjango/post_list.html',context={'page':page ,
    'next_page_url':next_url,
    'prev_page_url':prev
    
     })

def tags_list(request):
    tags =Tag.objects.all()
    return render(request,'blogdjango/tags_list.html',context={'tags':tags})


class PostDetail(DetailObjectMinxin, View):
    #inheri class DetailObjectMinxin
    model=Post
    template='./blogdjango/post_detail.html'

class TagDetail(DetailObjectMinxin, View):
    #inheri class DetailObjectMinxin
    model=Tag
    template='blogdjango/tag_detail.html'

class PostCreate(LoginRequiredMixin, View, CreateObjectMixin ):
    modelForm=PostForm
    template ='blogdjango/post_create.html'
    raise_exception =True
    # def get(self,request):
    #     form = PostForm()
    #     return render(request,'blogdjango/post_create.html',context={'form':form})

    # def post(self,request):
    #     bound_form =PostForm(request.POST)

    #     if bound_form.is_valid():
    #         new_post = bound_form.save()
    #         return redirect(new_post)
    #     return render(request,'blogdjango/post_create.html',context={'form':bound_form})

class TagCreate(LoginRequiredMixin, View, CreateObjectMixin):

    modelForm=TagForm
    template='blogdjango/tag_create.html'
    raise_exception =True


    # def get(self,request):
    #     form=TagForm()
    #     return render(request,'blogdjango/tag_create.html',context={'form':form})

    # def post(self, request):
    #     bound_form =TagForm(request.POST)

    #     if bound_form.is_valid():
    #         new_tag = bound_form.save()
    #         return redirect(new_tag)
    #     return render(request,'blogdjango/tag_create.html',context={'form':bound_form})

class TagUpdate(LoginRequiredMixin, View, UpdateObjectMixin):
    model =Tag
    form_class =TagForm
    template ='blogdjango/tag_update.html'
    raise_exception =True
    # def get(self,request,slug):
    #     tag = get_object_or_404(Tag,slug__iexact=slug)
    #     bound_form = TagForm(instance=tag)
    #     return render(request,'blogdjango/tag_update.html',context={'form':bound_form,'tag':tag})
    
    # def post(self,request,slug):

    #     tag = get_object_or_404(Tag,slug__iexact=slug)

    #     bound_form = TagForm(request.POST, instance=tag)

    #     if(bound_form.is_valid()):
    #         new_tag = bound_form.save()
    #         return redirect(new_tag)

    #     return render(request,'blogdjango/tag_update.html',context={'form':bound_form,'tag':tag})

class PostUpdate(LoginRequiredMixin, View, UpdateObjectMixin):
    model = Post
    form_class = PostForm
    template = 'blogdjango/post_update.html'
    raise_exception =True

class TagDelete(LoginRequiredMixin, View, DeleteObjectMixin):
    model = Tag
    template = 'blogdjango/tag_delete.html'
    redirect_url = 'tags_list_url'
    raise_exception =True

    # def get(self,request,slug):

    #     tag = get_object_or_404(Tag,slug__iexact=slug)

    #     return render(request,'blogdjango/tag_delete.html',context={'tag':tag})  
    
    # def post(self,request,slug):

    #     tag = get_object_or_404(Tag,slug__iexact=slug)
    #     tag.delete()

    #     return redirect(reverse('tags_list_url'))
class PostDelete(LoginRequiredMixin, View, DeleteObjectMixin, ):
    model = Post
    template = 'blogdjango/post_delete.html'
    redirect_url = 'post_list_url'
    raise_exception =True


