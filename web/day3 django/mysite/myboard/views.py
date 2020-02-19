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
    def get(self, request, pk, mode):
        if mode == 'list':
            data=Board.objects.all()
            username=request.session.get('username','')
            context={'data':data, 'username':username}
            return render(request, 'myboard/list.html', context)
        
        elif mode == 'detail':
            p=get_object_or_404(Board, pk=pk)
            p.cnt += 1
            p.save()
            return render(request, 'myboard/detail.html', {'p':p})
        
        elif mode == 'add':
            form = BoardForm()
            
        elif mode == 'edit':
            board = get_object_or_404(Board, pk=pk)
            form = BoardForm(instance=board)

        else : # 예상에 없을때 -> 오류 발생
            return HttpResponse('error page')
            
        return render(request, "myboard/edit.html", {"form":form})

    def post(self, request, pk, mode):

        username = request.session["username"]
        user = User.objects.get(username=username)
                    
        if pk == 0:
            form = BoardForm(request.POST)
        else:
            board = get_object_or_404(Board, pk=pk)
            form = BoardForm(request.POST, instance=board)
            
         
#         form.img = request.FILES.get('img') # 사진 파일명 저장
#         if form.img != None: # 파일 올렸으면 저장.
#             file = request.FILES['img']
#             filename = file._name
#             filepath = settings.BASE_DIR + "/static/" + filename
#             fp = open(filepath, "wb")
#             for chunk in file.chunks() :
#                 fp.write(chunk)
#             fp.close()
            
        if form.is_valid():
            board = form.save(commit=False) # 저장만 하고 커밋은 안함.
#             print(board.img)
            
#             form.img = request.FILES.get('img') # 사진 파일명 저장
#             if form.img != None: # 파일 올렸으면 저장.
#                 file = request.FILES['img']
#                 filename = file._name
#                 filepath = settings.BASE_DIR + "/static/" + filename
#                 fp = open(filepath, "wb")
#                 for chunk in file.chunks() :
#                     fp.write(chunk)
#                 fp.close()
            
            
#             board.img = form.img
            if pk == 0:
                board.author = user
            board.save()
            return redirect("myboard:myboard", 0, 'list')
        return render(request, "myboard/edit.html", {"form": form})