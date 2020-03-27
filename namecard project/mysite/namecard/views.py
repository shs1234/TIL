from django.shortcuts import render, redirect
from .models import Namecard
from django.http import HttpResponse
# Create your views here.

def index(request):
    if request.method == 'GET':
        isdel = request.GET.get('del', '')
        if isdel !='':
            Namecard.objects.filter(pk=isdel).delete()
            return redirect('/namecard')

        issearch = request.GET.get('option', '')
        if issearch !='':
            field = request.GET.get('field', '')
            if issearch=='name':
                data = Namecard.objects.filter(name=field)
            elif issearch=='category' :
                data = Namecard.objects.filter(category=field)
            else :
                data = Namecard.objects.all()
            context = {'data': data}
            return render(request, 'namecard/index.html', context)

        data = Namecard.objects.all()
        context = {'data': data}
        return render(request, 'namecard/index.html', context)

    else :
        isadd = request.POST.get('add', '')
        if isadd != '':
            name = request.POST['name']
            email = request.POST['email']
            mobile = request.POST['mobile']
            address = request.POST['address']
            category = request.POST['category']
            image = request.POST['file']

            Namecard(name=name, email=email, mobile=mobile,
                     address=address, category=category, image=image).save()

        return redirect('/namecard')