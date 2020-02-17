from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import json
from myapp.models import User
# Create your views here.

# jquery 공부해보기

def index(request):
    return HttpResponse('hello django')

def test(request):
    data= {'s':{'img':'test.png'}, 'list':[1,2,3,4,5]}
    return render(request,'template.html', data)

def login(request):
    id = request.GET['id']
    pwd = request.GET['pwd']
    if id == pwd:
        request.session['user']=id
        return service(request)
    else : 
        return redirect('/static/login.html')
    
def logout(request):
    request.session['user']=''
#     request.session.pop('user')
    return redirect('/static/login.html')

@csrf_exempt      #csrf 오류 무시함
def uploadimage(request):
    file = request.FILES['file1']
    filename=file._name
    fp=open(settings.BASE_DIR + '/static/' + filename, 'wb')
    for chunk in file.chunks():
        fp.write(chunk)
    fp.close()
#     result=face.faceverification(settings.BASE_DIR + '/static/' + filename)
#     result = faceverification(settings.BASE_DIR + '/static/' + filename)
    
#     if result != '':
#         request.session['user']=result
#         return redirect('/service')
    
    return redirect('/static/login.html')
    
def service(request):
    if request.session.get('user','')=='':
        return redirect('/static/login.html')
        
    html='main service<br>'+request.session.get('user')+'님 환영합니다. <a href=/logout>로그아웃</a>'
    return HttpResponse(html)

def calc(request):
    op1 = request.GET['op1']
    op2 = request.GET['op2']
    result = int(op1) + int(op2)

    return HttpResponse( json.dumps({'result': result}), content_type='application/json')
    #return JsonResponse({'result': result})
    
def listUser(request):
    if request.method=='GET':
        q=request.GET.get('q',"")
        data=User.objects.all()
        if q!="":
            data=User.objects.all().filter(name__contains=q)
        return render(request,'template2.html', {'data':data})
    
        userid=request.GET.get('userid','')
        if userid!='':
            User.objects.all().get(userid=userid).delete()
            return redirect('/listuser')
    
    else :
        # db insert
        userid = request.POST['userid']
        name = request.POST['name']
        age = request.POST['age']
        hobby = request.POST['hobby']
        
        User(userid=userid, name=name, age=age, hobby=hobby).save()
        
        return redirect('/listuser')
    