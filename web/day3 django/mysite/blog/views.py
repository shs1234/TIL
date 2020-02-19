from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from blog.models import Post
from django.views.generic import View
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.forms import Form, CharField, Textarea, ValidationError
from django import forms
from .forms import PostForm

# url 더 줄이기. <mode> 사용. 리스트+디테일+add+edit을 하나로.

# Create your views here.

def index(request):
    return HttpResponse('welcome')

# def postlist(request):
#     data=Post.objects.all()
#     username=request.session.get('username','')
#     context={'data':data, 'username':username}
#     return render(request, 'blog/postlist.html', context)

# def detail(request, pk):
# #     p=Post.objects.get(pk=pk)
#     p=get_object_or_404(Post, pk=pk)
#     return render(request, 'blog/detail.html', {'p':p})
        
    
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
    def get(self, request, pk, mode):
        if mode == 'list':
            data=Post.objects.all()
            username=request.session.get('username','')
            context={'data':data, 'username':username}
            return render(request, 'blog/postlist.html', context)
        
        elif mode == 'detail':
            p=get_object_or_404(Post, pk=pk)
            return render(request, 'blog/detail.html', {'p':p})
        
        elif mode == 'add':
            form = PostForm()
            
        elif mode == 'edit':
            post = get_object_or_404(Post, pk=pk)
            form = PostForm(instance=post)

        else : # 예상에 없을때 -> 오류 발생
            return HttpResponse('error page')
            
        return render(request, "blog/editpost.html", {"form":form})

    def post(self, request, pk, mode):

        username = request.session["username"]
        user = User.objects.get(username=username)

        if pk == 0:
            form = PostForm(request.POST)
        else:
            post = get_object_or_404(Post, pk=pk)
            form = PostForm(request.POST, instance=post)

        if form.is_valid():
            post = form.save(commit=False) # 저장만 하고 커밋은 안함.
            if pk == 0:
                post.author = user
                post.save()
            else :
                post.publish()
            return redirect("blog:viewblog", 0, 'list')
        return render(request, "blog/editpost.html", {"form": form})