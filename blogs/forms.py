from django.forms import ModelForm
from django import forms 
from .models import Blog,Tags,Comment,Report

class BlogForm(ModelForm):

    class Meta:
        model=Blog
        #exclude =['voted']
        #exclude = ()
        #fields="__all__"
        fields=['title','content','tags','featured_image','analysis','writer',]
        #adding widgets
        widgets={'tags':forms.CheckboxSelectMultiple(),

        }

  
     
   

     
    #adding classes through method overriding
    def __init__(self,*args, **kwargs):
        super(BlogForm,self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update(
            {'class':'form-input'})
        
        self.fields['content'].widget.attrs.update(
            {'class':'form-input-textarea'}
        )

        self.fields['tags'].widget.attrs.update(
            {'class':'form-input-tag'}
        )

     

        self.fields['featured_image'].widget.attrs.update(
            {'class':'form-input'}
        )
        self.fields['analysis'].widget = forms.HiddenInput()
        self.fields['analysis'].label = ""
        self.fields['writer'].widget = forms.HiddenInput()
        self.fields['writer'].label = ""
        #for name,field in self.fields.items:
            #field.widget.attrs.update({'class':'input'})


#comment Form

class CommentForm(ModelForm):
    class Meta:
        model=Comment
        #exclude =['voted']
        #exclude = ()
        #fields="__all__"
        fields=['commentor','blog','comment',]
        #adding widgets
      
  
     
   

     
    #adding classes through method overriding
    def __init__(self,*args, **kwargs):
        super(CommentForm,self).__init__(*args, **kwargs)
        self.fields['comment'].widget.attrs.update(
            {'class':'form-input'})
   
        self.fields['commentor'].widget = forms.HiddenInput()
        self.fields['commentor'].label = ""
        self.fields['blog'].widget = forms.HiddenInput()
        self.fields['blog'].label = ""
        #for name,field in self.fields.items:
            #field.widget.attrs.update({'class':'input'})



class ReportForm(ModelForm):
    class Meta:
        model=Report
        #exclude =['voted']
        #exclude = ()
        #fields="__all__"
        fields=['report']
        #adding widgets
      
  
     
   

     
    #adding classes through method overriding
    def __init__(self,*args, **kwargs):
        super(ReportForm,self).__init__(*args, **kwargs)
 
        for names,field in self.fields.items():
            field.widget.attrs.update({'class':'form-input'})

