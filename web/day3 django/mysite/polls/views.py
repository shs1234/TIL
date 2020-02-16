from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = '<br><br>'.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

def detail(request, question_id):
    
    return HttpResponse('%s번 질문을 보고 있습니다.'%question_id)

def results(request, question_id):
    response = '%s번 질문의 결과를 보고 있습니다.'
    return HttpResponse(response%question_id)

def vote(request, question_id):
    return HttpResponse('%s번 질문에 투표하고 있습니다.'%question_id)