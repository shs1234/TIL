from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from blog.models import Post
from django.views.generic import View
from django.contrib.auth import authenticate
from django.forms import Form


# Create your views here.

def index(request):
    return HttpResponse('welcome')

def list(request):
    data=Post.objects.all()
    username=request.session.get('username','')
    context={'data':data, 'username':username}
    return render(request, 'blog/list.html', context)

def detail(request, pk):
#     p=Post.objects.get(pk=pk)
    p=get_object_or_404(Post, pk=pk)
    return render(request, 'blog/detail.html', {'p':p})

# class PostEditView(View):
#     def get(self, request, pk):
#         post = get_object_or_404(Post, pk)
#         form = PostForm(initi)
#         return
    
#     def post(self, request, pk):
#         return
    

# class PostForm(Form):
#     title=CharField(label='제목', max_length=20)
#     text=CharField(label='내용', widget=textarea)
    
class AddPost(View):
    def get(self, request):
        return render(request, 'blog/edit.html')
    
    def post(self, request):
        username = request.session['username']
        user=Post.objects.get(username=username)
        title=request.POST.get('title')
        text=request.POST.get('text')
        Post.objects.create(title=title, text=text, author=user)
        
        return redirect('list')
        
    
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
        return redirect('list')