from django.shortcuts import render, redirect
from .models import *
from .forms import *
# Create your views here.

def index(request): 
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            #jesli chce wrocic do innej strony
            return redirect("/")

    posts = Post.objects.all()
    comms = Post_comments.objects.all()
    reacs = Post_reactions.objects.all()

    contex = {'posts' : posts,'comms':comms, 'reacs':reacs,'form':form}

    return render(request,'PostApp/index.html',contex)


def add_post(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
            
    contex = {'form':form}
    return render(request,'PostApp/add_post.html',contex)

def delete_post(request,pk):
    del_post = Post.objects.get(id=pk)

    if request.method == 'POST':
        del_post.delete()
        return redirect("/")

    contex = {'post':del_post}
    return render(request,'PostApp/delete_post.html',contex)

def delete_com(request):
    pass