from django.dispatch import receiver
from django.db.models.signals import post_save

from django.contrib.auth.models import User
from .models import *

@receiver(post_save,sender = User)
def create_profile(sender,instance,created ,**kwargs):
    if created:
        UserProfile.objects.create(user=instance,profile_image = 'static/images/profile.jpg')
        print('Created')
        pass

#----- W sumie mozna ty chyba zrobic jako jedną funkcje

@receiver(post_save,sender = User)
def update_profile(sender,instance,created ,**kwargs):

    if created == False:
        instance.userprofile.save()
        print('Updated')
        pass

#uzycie bez dekoratora
#post_save(update_profile,sender = User)