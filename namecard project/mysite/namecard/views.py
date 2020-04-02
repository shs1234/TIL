from django.shortcuts import render, redirect
from django.conf import settings
from .models import Namecard
# Create your views here.

def index(request):
    if request.method == 'GET':
        isimg = request.GET.get('img', '')
        if isimg != '':
            data = Namecard.objects.filter(name=isimg)
            print(data)
            context = {'data': data}
            return render(request, 'namecard/img.html', context)

        isdel = request.GET.get('del', '')
        if isdel != '':
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

            file = request.FILES.get('file', '')    # 파일이 올라왔는지 확인.

            if file!='':
                filename = file._name
                filepath = settings.BASE_DIR + "/static/" + filename
                fp = open(filepath, "wb")
                for chunk in file.chunks() :
                    fp.write(chunk)
                fp.close()
                image = filename
                Namecard(name=name, email=email, mobile=mobile,
                         address=address, category=category, image=image).save()
                return redirect('/namecard')


            Namecard(name=name, email=email, mobile=mobile,
                     address=address, category=category).save()

        return redirect('/namecard')