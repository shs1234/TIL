from django.urls import path
from . import views

# path('test', views.test) : 주소, 그 주소로 가면 사용되는 함수 명

urlpatterns = [
    path('', views.index),
    
    path('calcform', views.calcForm),
    path('calc', views.calc),
    
    path('loginform', views.loginform),
    path('login', views.login),
        
    path('runpythonform', views.runpythonform),
    path('runpython', views.runpython),
    
    path('uploadform', views.uploadForm),
    path('upload', views.upload),
]
