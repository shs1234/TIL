from django.shortcuts import render, redirect
from .models import Namecard
from django.http import HttpResponse
# Create your views here.

def index(request):
    if request.method == 'GET':
        data = Namecard.objects.all()
        context = {'data': data}
        return render(request, 'namecard/index.html', context)

    else :
        isadd = request.POST.get('add', '')
        # print(request.POST)
        # print(isadd)
        if isadd != '':
            name = request.POST['name']
            email = request.POST['email']
            mobile = request.POST['mobile']
            address = request.POST['address']

            Namecard(name=name, email=email, mobile=mobile, address=address).save()
        return redirect('/namecard')