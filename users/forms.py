from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','email','username','password1','password2']
    
        labels={
            'first_name':'Full Name'
        }
    #adding classes through method overriding
    def __init__(self,*args, **kwargs):
        super(CustomUserCreationForm,self).__init__(*args, **kwargs)
        for names,field in self.fields.items():
            field.widget.attrs.update({'class':'form-input'})

class CustomProfileCreationForm(ModelForm):
    class Meta:
        model=Profile
        fields=['full_name','username','email','phone_no','address','bio','profile_picture']
    
        labels={
            'first_name':'Full Name'
        }
    #adding classes through method overriding
    def __init__(self,*args, **kwargs):
        super(CustomProfileCreationForm,self).__init__(*args, **kwargs)
        for names,field in self.fields.items():
            field.widget.attrs.update({'class':'form-input'})

