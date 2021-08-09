from django.forms.widgets import HiddenInput
from django.http.request import QueryDict
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView,DetailView,UpdateView,FormView,ListView

from django.forms import inlineformset_factory

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

from .models import *
from django.contrib.auth.models import User
from .forms import *
# Create your views here.

#class-based views

#generic-class-based views
class Dashboard(TemplateView):
    template_name = 'PostApp/dashboard.html'
    model = Post
    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['posts'] = Post.objects.all()
        contex['comments'] = Post_comments.objects.all()
        return contex

    def get(self,request,*args,**kwargs):
        posts = Post.objects.all()
        contex = {'posts':posts}
        return render(request,'PostApp/dashboard.html',contex)

    def post(self,request):
        # Post.objects.create()
        pass

# function-based views

@login_required(login_url='login')
def index(request): 
    author = User.objects.get(username = request.user)
    form = PostForm(initial={'author': author,'pub_date' : timezone.now})
    commentForm = CommentForm(initial={'author': author,'pub_hour' : timezone.now})

    if request.method == 'POST':
        if request.POST.get('form_type') == 'add_post':
            form = PostForm(request.POST)
            print(request.POST)
            if form.is_valid():
                form.save()
                #jesli chce wrocic do innej strony
                return redirect("/")
        elif request.POST.get('form_type') == 'add_comm':
            commentForm = CommentForm(request.POST)
            print(request.POST)
            if commentForm.is_valid():
                commentForm.save()
                return redirect('/')

    posts = Post.objects.all()
    contex = {'posts' : posts,'form':form,'commentForm':commentForm}

    return render(request,'PostApp/index.html',contex)

def test(request):
    form =  MyForm(initial={'author' : request.user})
    print(request.POST)
    contex = {'form':form}
    return render(request,'PostApp/test.html',contex)

# def add_comment(request):
#     form = Post_commForm()
#     if request.method == 'POST':
#         form =  Post_commForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/')

#     comments = Post_comments.objects.all()
#     contex ={'form_com':form,'comments':comments, 'my_number' : 123}
#     return render(request,'PostApp/comment_section.html',contex)

@login_required(login_url='login')
def add_post(request):
    form = PostForm()
    Post.objects.get(request)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
            
    contex = {'form':form}
    return render(request,'PostApp/add_post.html',contex)
    
@login_required(login_url='login')
def delete_post(request,pk):
    del_post = Post.objects.get(id=pk)

    if request.method == 'POST':
        del_post.delete()
        return redirect("/")

    contex = {'post':del_post}
    return render(request,'PostApp/delete_post.html',contex)

@login_required(login_url='login')
def delete_com(request):
    pass



def about_me(requset):
    return render(requset,'PostApp/about_me.html')

def profile(request,pk):
    # user = UserProfile.objects.get_or_create(user_id = pk)
    user =  request.user.userprofile
    form = ProfileForm(instance=user)
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()

    contex = {'profile':profile,'form':form}

    return render(request,'PostApp/profile.html',contex)

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form =  CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            print(request.POST)
            if form.is_valid():
                print('po valid')
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request,'Account was created for ' + username)
                return redirect('login')

        contex = {'form':form}
        return render(request,'PostApp/register.html',contex)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            
            user = authenticate(request,username = username , password = password)
            if user is not None:
                login(request,user)
                return redirect('index')
            else:
                messages.info(request,'Username OR password is incorrect')

        contex = {}
        return render(request,'PostApp/login.html',contex)

def logoutUser(request):
    logout(request)
    return redirect('login')