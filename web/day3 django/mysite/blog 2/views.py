from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from blog.models import Post
from django.views.generic import View
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.forms import Form, CharField, Textarea, ValidationError
from django import forms
from .forms import PostForm

# forms 모듈화. append edit 기능 합치기

# Create your views here.

def index(request):
    return HttpResponse('welcome')

def postlist(request):
    data=Post.objects.all()
    username=request.session.get('username','')
    context={'data':data, 'username':username}
    return render(request, 'blog/postlist.html', context)

def detail(request, pk):
#     p=Post.objects.get(pk=pk)
    p=get_object_or_404(Post, pk=pk)
    return render(request, 'blog/detail.html', {'p':p})
        
    
class LoginView(View):
    def get(self, request):
        return render(request, 'blog/login.html')
    
    def post(self, request):
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user == None:
            return redirect('login')
        request.session['username']=username
        return redirect('blog:postlist')


    
class EditPost(View) :
    def get(self, request, pk):
        if pk == 0 :
            form = PostForm()
        else :
            post = get_object_or_404(Post, pk=pk)
            form = PostForm(instance=post)
        return render(request, "blog/editpost.html", {"form":form})

    def post(self, request, pk):

        username = request.session["username"]
        user = User.objects.get(username=username)

        if pk == 0:
            form = PostForm(request.POST)
        else:
            post = get_object_or_404(Post, pk=pk)
            form = PostForm(request.POST, instance=post)

        if form.is_valid():
            post = form.save(commit=False)
            if pk == 0:
                post.author = user
                post.save()
            else :
                post.publish()
            return redirect("blog:postlist")
        return render(request, "blog/editpost.html", {"form": form})






    
# class EditPost(View):
#     def get(self, request, pk):
#         if pk==0:  # add
#             form = PostForm()
#         else :   # edit
#             post = get_object_or_404(Post, pk=pk)
#             form = PostForm(initial={'title':post.title, 'text':post.text})
#         return render(request, 'blog/editpost.html', {'form':form})

#     def post(self, request, pk):
#         form = PostForm(request.POST)
#         if form.is_valid():
#             if pk==0:   # add
#                 username = request.session['username']
#                 user=User.objects.get(username=username)
#                 Post.objects.create(title=form['title'].value(), text=form['text'].value(), author=user)
         
#             else :
#                 post = get_object_or_404(Post, pk=pk)
#                 post.title = form['title'].value()
#                 post.text = form['text'].value()
#                 post.publish()
#             return redirect('blog:postlist')
#         return render(request, 'blog/editpost.html', {'form':form})


