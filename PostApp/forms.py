from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import fields
from django.forms import ModelForm,Form
from django.http import request
from .models import *

from django.utils import timezone
from ckeditor.widgets import CKEditorWidget

class PostForm(ModelForm):
    # content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Post
        fields = '__all__'
        widgets =  {
        'author' : forms.HiddenInput(),
        'pub_date':forms.HiddenInput(),
        'content' :forms.CharField(widget=CKEditorWidget()),
        }

class MyForm(Form):
    author = forms.CharField(label = 'Nazwa użytkowania: ',max_length=100, widget=forms.HiddenInput())
    pub_date = forms.DateTimeField(label = 'Data publikacji: ',widget=forms.HiddenInput()) 
    content = forms.CharField(label = 'Treść: ',max_length=200)

class CommentForm(ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Post_comments
        fields = '__all__'
        widgets =  {
        # 'post': forms.HiddenInput(),
        'author' : forms.HiddenInput(),
        'pub_date':forms.HiddenInput(),
        }
        
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        # fields = '__all__'

class ProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
        exclude = ['user']