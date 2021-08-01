from django.db.models import fields
from django.forms import ModelForm
from .models import *

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

        #Gdy nie chcemy wprowadzac wszytstkich pól a tylko wybrane 
        # fields = ['author','pub_date']

class Post_commForm(ModelForm):
    class Meta:
        model = Post_comments
        fields = '__all__'
        

class Post_reactionForm(ModelForm):
    class Meta:
        model = Post_reactions
        fields = '__all__'
