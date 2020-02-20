from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import View
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.forms import Form, CharField, Textarea, ValidationError
from django import forms
from . import models

def validator(value):
    if len(value) < 2 : raise ValidationError('길이가 너무 짧습니다.')
    
class BoardForm(forms.ModelForm):
    class Meta:
        model = models.Board
        fields = ['title', 'text', 'img', 'category']

    def __init__(self, *args, **kwargs):
        super(BoardForm, self).__init__(*args, **kwargs)
        self.fields['title'].validators = [validator]