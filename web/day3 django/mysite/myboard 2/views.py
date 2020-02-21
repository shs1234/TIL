from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from myboard.models import Board
from django.views.generic import View
from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.forms import Form, CharField, Textarea, ValidationError
from django import forms
from .forms import BoardForm

# Create your views here.

# 조회수 이미지 n개의 게시판 완성할것.

class BoardView(View) :
    def get(self, request, category, pk, mode):
        if mode == 'list':
            data=Board.objects.all().filter(category=category)
            user = User.objects.get(username='admin')
            
            context={'data':data, 'username':user, 'category':category}
            return render(request, 'myboard/list.html', context)
        
        elif mode == 'detail':
            p=get_object_or_404(Board, pk=pk)
            p.cnt += 1
            p.save()
            return render(request, 'myboard/detail.html', {'p':p, 'category':category})
        
        elif mode == 'add':
            form = BoardForm()
            
            
        elif mode == 'edit':
            board = get_object_or_404(Board, pk=pk)
            form = BoardForm(instance=board)

        else : # 예상에 없을때 -> 오류 발생
            return HttpResponse('error page')
            
        return render(request, "myboard/edit.html", {"form":form, 'category':category})

    def post(self, request, category, pk, mode):

        username = request.session["username"]
        user = User.objects.get(username=username)
                    
        if pk == 0:
            form = BoardForm(request.POST)
        else:
            board = get_object_or_404(Board, pk=pk)
            form = BoardForm(request.POST, instance=board)
                     
        if form.is_valid():
            board = form.save(commit=False) # 저장만 하고 커밋은 안함.

            if pk == 0:
                board.author = user
            
            file = request.FILES.get('file','')    # 파일이 올라왔는지 확인.
            if file!='':
                filename = file._name
                filepath = settings.BASE_DIR + "/static/" + filename
                fp = open(filepath, "wb")
                for chunk in file.chunks() :
                    fp.write(chunk)
                fp.close()
                board.img = filename     #파일이 있을경우 img에 파일 이름 저장.
                
            board.category = category
            board.save()
            return redirect("myboard:myboard", category, 0, 'list')
        return render(request, "myboard/edit.html", {"form": form})