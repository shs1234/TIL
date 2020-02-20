from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.urls import reverse

from . import forms
from . import models
from . import apps
from django.urls import resolve


def page(request):
    datas = [{"id":1, "name":"홍길동1"},
            {"id":2, "name":"홍길동2"},
            {"id":3, "name":"홍길동3"},
            {"id":4, "name":"홍길동4"},
            {"id":5, "name":"홍길동5"},
            {"id":6, "name":"홍길동6"},
            {"id":7, "name":"홍길동7"},
            ]
    page = request.GET.get("page", 1)
    p = Paginator(datas, 3)
    subs = p.page(page)  #(page-1)*3:page*3
    return render(request, "myboard/page,html", {"datas":subs})

def ajaxdel(request):
    pk = request.GET.get('pk')
    board = models.Board.objects.get(pk=pk)
    #board.delete()
    return JsonResponse({'error':'0'})

def ajaxget(request):
    page = request.GET.get("page",1)
    
    datas = models.Board.objects.all().filter(category='common')
    page = int(page)
    subs = datas[(page-1)*3:(page)*3]
    
    datas = {"datas" : [{"pk":data.pk, "title":data.title, "cnt":data.cnt} for data in subs]}
    
    return JsonResponse(datas)
    #p = Paginator(datas, 3)
    #subs = p.page(page)


class BoardView(View) :
    def get(self, request, category, pk, mode):
        if  mode == 'add' :
            form = forms.BoardForm()
        elif mode == 'list' :
#             username = request.session["username"]
            user = User.objects.get(username='admin')
            data = models.Board.objects.all().filter(category=category)
            
            page = request.GET.get("page", 1)
            p = Paginator(data, 3)
            subs = p.page(page)  #(page-1)*3:page*3
            
            context = {"datas": subs, "username": user, "category": category}
            
            return render(request, "myboard/list.html", context)
        elif mode ==  "detail" :
            p = get_object_or_404(models.Board, pk=pk)
            p.cnt += 1
            p.save()
            return render(request, "myboard/detail.html", {"d": p,"category":category})
        elif mode == "edit" :
            board = get_object_or_404(models.Board, pk=pk)
            form = forms.BoardForm(instance=board)
        else :
            return HttpResponse("error page")

        return render(request, "myboard/edit.html", {"form":form})

    def post(self, request, category, pk, mode):

#         username = request.session["username"]
        user = User.objects.get(username='admin')

        if pk == 0:
            form = forms.BoardForm(request.POST)
        else:
            board = get_object_or_404(models.Board, pk=pk)
            form = forms.BoardForm(request.POST, instance=board)

        if form.is_valid():
            board = form.save(commit=False)
            if pk == 0:
                board.author = user
            board.category = category
            board.save()
            return redirect("myboard", category, 0, 'list')
        return render(request, "myboard/edit.html", {"form": form})