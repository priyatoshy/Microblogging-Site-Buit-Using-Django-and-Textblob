from django.db import models
from django.contrib.auth.models import User
import uuid
from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from .models import Profile
from django.core.mail import send_mail
from django.conf import settings
# Create your models here.

#sender
#function(sender model )
#sender model under operation
#instance is the particular model object under operation
#created is a boolean value(if it is new instance or not)


#@receiver(post_save,sender=User)
def CreateProfile(sender,instance,created,**kwargs):
    if created:
        user=instance
        #print(f"\n\n\n{instance}\n\n\n")
        profile=Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            full_name=user.first_name,

        )
        subject=f"WELCOME {user.username}"
        message="WE WELCOME YOU"
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [profile.email],
            fail_silently=False

        )
        
#@receiver(post_save,sender=User)
def UpdateProfile(sender,instance,created,**kwargs):
    if created==False:
        profile=instance
        user=profile.user
        #print(f"\n\n\n{instance}\n\n\n")
        user.first_name=profile.full_name
        user.username=profile.username
        user.email=profile.email
        user.save()


post_save.connect(UpdateProfile,sender=Profile)
#@receiver(post_delete,sender=Profile)
def delete_user(sender,instance,**kwargs):
    try:
        user = instance.user
        user.delete()
    except:
        pass

#connecting the signal method,our function and model
post_save.connect(CreateProfile,sender=User)

#post_delete.connect(delete_user,sender=Profile)
