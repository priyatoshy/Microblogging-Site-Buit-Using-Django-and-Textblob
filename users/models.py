from django.db import models
from django.contrib.auth.models import User
import uuid
from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
#from blogs.models import Tags
# Create your models here.
class Profile(models.Model):

    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    full_name=models.CharField(max_length=200,blank=True,null=True)
    username=models.CharField(max_length=200,blank=True,null=True)
    email=models.EmailField(max_length=200,blank=True,null=True)
    phone_no=models.CharField(blank=True,null=True,max_length=13)
    address=models.TextField(blank=True,null=True)
    profile_picture=models.ImageField(blank=True,null=True,upload_to='profiles/',default="profiles/default.png")
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    

    created_on=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    roles=(
        ('BLOGGER','BLOGGER'),
    

     )
    user_role=models.CharField(max_length=255,blank=True,choices=roles,default='BLOGGER') 
    interests=models.ManyToManyField('Interests',blank=True)
    bio=models.TextField(default="Writing...............")
    def __str__(self):
         if self.full_name: 
            return self.full_name
         elif self.user:
            return f"{self.user}"
         else:
            return f"{self.id}"
   
    

#sender
#function(sender model )
#sender model under operation
#instance is the particular model object under operation
#created is a boolean value(if it is new instance or not)


#a session id is created everytime we log in
#it is stored in the browser cookies
#when we delete it ,we are automatically logged out
#it is stored in both database and cookies
#we use a cookie based authentication


class Interests(models.Model):
     id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
     #owner=models.ForeignKey('Profile',blank=True,null=True)
     title=models.CharField(max_length=50)

     def __str__(self):
         return self.title


#messaging functionality
class Messages(models.Model):
   id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
   sender=models.ForeignKey(Profile,on_delete=models.CASCADE)
   receiptient=models.ForeignKey(Profile,on_delete=models.CASCADE,related_name="message")
   #related name will allow us to access to the field later on and
   #avoid conflict 
   name=models.CharField(max_length=200,blank=True)
   email=models.EmailField(null=True,blank=True)
   text=models.TextField()
   created_on=models.DateTimeField(auto_now_add=True,null=True,blank=True)
   status=models.BooleanField(default=False)

   class Meta:
      ordering=['status','-created_on']
   def __str__(self):
       message=self.text[0:10]
       return message