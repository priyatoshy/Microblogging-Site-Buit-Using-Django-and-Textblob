from django.db import models
import uuid

from django.db.models.deletion import CASCADE
from users.models import Profile
#from users.models import Profile
# Create your models here.


class Blog(models.Model):
     id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
     writer=models.ForeignKey(Profile,null=True,blank=True,on_delete=models.CASCADE)
     title=models.CharField(max_length=255)
     content=models.TextField(max_length=300)
     tags=models.ManyToManyField('Tags',blank=True)
   
     rate=models.IntegerField(default=0)
     voted=models.IntegerField(default=1)
     created_on=models.DateTimeField(auto_now_add=True,null=True,blank=True)
     featured_image=models.ImageField(blank=True,null=True,default="profiles/default.png") 
     analysis=models.CharField(blank=True,null=True,max_length=500)
     class Meta:
        ordering = ('-rate', )

     def __str__(self):
         return self.title
     

class Tags(models.Model):
     id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
     
     title=models.CharField(max_length=50)

     def __str__(self):
         return self.title


class Comment(models.Model):
     id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
     likes=models.IntegerField(default=0)
     commentor=models.ForeignKey(Profile,null=True,blank=True,on_delete=models.CASCADE)
     blog=models.ForeignKey('Blog',null=True,blank=True,on_delete=models.SET_NULL)
     comment=models.TextField(max_length=50)
     created_on=models.DateTimeField(auto_now_add=True,null=True,blank=True)
     
     
     class Meta:
        ordering = ('-likes', )
     
     def __str__(self):
         return self.comment

class ReactionHistory(models.Model):

    blog=models.ForeignKey('Blog',null=True,blank=True,on_delete=models.CASCADE)
    profile=models.ForeignKey(Profile,null=True,blank=True,on_delete=models.CASCADE)
    status=models.BooleanField(default=False)
    

class Report(models.Model):
     id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
     reported_by=models.ForeignKey(Profile,null=True,blank=True,on_delete=models.CASCADE)
     blog=models.ForeignKey('Blog',null=True,blank=True,on_delete=models.SET_NULL)
     report=models.TextField(max_length=50)
     created_on=models.DateTimeField(auto_now_add=True,null=True,blank=True)
     
     
     class Meta:
        ordering = ('-created_on', )
        unique_together=[['blog','reported_by']]
     
     def __str__(self):
         return self.report


class BlockedContent(models.Model):
     id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
     blocker=models.OneToOneField(Profile,null=True,blank=True,on_delete=models.CASCADE)
     blog=models.ManyToManyField('Blog',blank=True)
     blocked_on=models.DateTimeField(auto_now_add=True,null=True,blank=True)
   
     
     class Meta:
        ordering = ('-blocked_on', )
        #unique_together=[['blog','blocker']]
     
     def __str__(self):
         return self.blocker

class Bookmark(models.Model):
     id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
     owner=models.ForeignKey(Profile,null=True,blank=True,on_delete=models.CASCADE)
     blog=models.ManyToManyField('Blog',blank=True)
     saved_on=models.DateTimeField(auto_now_add=True,null=True,blank=True)
     
     
     class Meta:
        ordering = ('-saved_on', )
        #unique_together=[['blog','blocker']]
     
     def __str__(self):
         return self.owner
       


class Followable(models.Model):
      
      account=models.OneToOneField(Profile,on_delete=models.CASCADE)
      

class Blocked(models.Model):
      
      blocked=models.OneToOneField(Profile,on_delete=models.CASCADE)

