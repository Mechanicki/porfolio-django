from typing import ForwardRef
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class Pseudo_User(models.Model):
    user = ForeignKey(User,on_delete=CASCADE,null=True)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50)
    profile_img = models.ImageField(null = True, blank = True)

    def __str__(self) -> str:
        return self.name +' '+ self.surname + ' "' + self.nickname + '"' 

        

class Post(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE ,null=True)
    pub_date = models.DateTimeField(default=timezone.now,null=True)
    content = RichTextField(blank=True,null=True)
    # content = models.CharField(max_length=200,null=True)

    def __str__(self) -> str:
        return 'post'


class Post_comments(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,blank=True,null=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE ,blank=True,null=True)
    content = RichTextField(blank=True,null=True)
    # content = models.TextField( max_length=200 ,blank=True,null=True)
    pub_date = models.DateTimeField(default=timezone.now,null=True)
    def __str__(self) -> str:
        return ' Comment '

class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE,  )
    profile_image = models.ImageField(null=True,blank = True)
    name =  models.CharField(max_length=100,null=True,blank = True)
    surname = models.CharField(max_length=100,null=True,blank = True)
    nickname = models.CharField(max_length=100,null=True,blank = True)
    email = models.CharField(max_length=100 ,null=True,blank = True)

    def __str__(self) -> str:
        return 'Profile'