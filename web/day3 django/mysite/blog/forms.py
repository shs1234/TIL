from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from blog.models import Post
from django.views.generic import View
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.forms import Form, CharField, Textarea, ValidationError
from django import forms


def validator(value):
    if len(value) < 5 : raise ValidationError('길이가 너무 짧습니다.')
    
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text']
