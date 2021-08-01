from typing import ForwardRef
from django.db import models
from django.utils import timezone


# Create your models here.
class Pseudo_User(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50)
    profile_img = models.ImageField(null = True, blank = True)

    def __str__(self) -> str:
        return self.name +' '+ self.surname + ' "' + self.nickname + '"' 

        

class Post(models.Model):
    author = models.ForeignKey(Pseudo_User,on_delete=models.CASCADE ,null=True)
    pub_date = models.DateField(default=timezone.now,null=True)
    # content = models.ForeignKey(Post_content)
    content = models.CharField(max_length=200,null=True)

    def __str__(self) -> str:
        return 'Post ' + self.author.nickname + ' ' + self.content


class Post_comments(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,blank=True,null=True)
    com_auth = models.ForeignKey(Pseudo_User,on_delete=models.CASCADE ,blank=True,null=True)
    comment_text = models.TextField(max_length=200 ,blank=True,null=True)
    pub_hour = models.DateTimeField(default= timezone.now(),null=True)
    def __str__(self) -> str:
        return self.com_auth.nickname  + ' Comment '


# TRZEBA JESZCZE ZROBIC TAK ABY MOZNA BYŁO DAC TYLKO JEDNEGO LIKE'A!
class Post_reactions(models.Model):
    auth_user = models.ForeignKey(Pseudo_User,on_delete=models.CASCADE ,blank=True,null=True)
    like_value = models.BooleanField(blank=True,null=True)

    post = models.ForeignKey(Post,null=True,on_delete=models.CASCADE)

    def __str__(self) -> str:
        
        if self.like_value:
            return 'Like ' + self.auth_user.name
        else:
            return 'Unlike ' + self.auth_user.name



# class Post_content(models.Model):
#     content = models.CharField(max_length=200)
    
#     def __str__(self) -> str:
#         pass