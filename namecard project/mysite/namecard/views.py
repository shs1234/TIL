from django.shortcuts import render
from .models import Namecard
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'namecard/index.html', {})

def list(request):
    return render(request, 'namecard/list.html', {})