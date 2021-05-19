from django import forms
from .models import Tag,Post
from django.core.exceptions import ValidationError 

class TagForm(forms.Form):
    # class Meta:
    #     model =Tag
    #     fields=['title','slug']
    #     widgets ={
    #         'title':forms.TextInput(attrs={'class':'form-control'}),
    #         'slug':forms.TextInput(attrs={'class':'form-control'})   
    #     } 
        
    # def clean_slug(self):
    #     print(5)
    #     new_slug =self.cleaned_data.get('slug').lower()
    #     if new_slug == 'create':
    #         print("nhan create")
    #         raise ValidationError('Slug may not be "create" ')
    #     if Tag.objects.filter(slug__iexact=new_slug).count():
    #         print("nhan unique")
    #         raise ValidationError(f'Slug should be UNIQUE. we have "{new_slug}" already')          
    #     return new_slug
    title =forms.CharField(max_length=255)
    slug =forms.SlugField(max_length=255)
    def save(self):
        new_tag = Tag.objects.create(
            title =self.cleaned_data.get('title'),
            slug = self.cleaned_data.get('slug')
        )
    
class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ['title','slug','body','tags']
        widgets ={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'slug':forms.TextInput(attrs={'class':'form-control'}) ,
            'body':forms.Textarea(attrs={'class':'form-control'}) ,
            'tags':forms.SelectMultiple(attrs={'class':'form-control'})   
        }
    def clean_slug(self):       
        new_slug =self.cleaned_data.get('slug').lower()
        if new_slug == 'create':
            raise ValidationError('Slug may not be aa "create" ')   
        print("chay xun day roi")     
        return new_slug
