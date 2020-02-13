from django.urls import path
from . import views

# path('test', views.test) : 주소, 그 주소로 가면 사용되는 함수 명

urlpatterns = [
    path('', views.index),
    path('test', views.test),
    path('login', views.login),
    path('logout', views.logout),
    path('uploadimage', views.uploadimage),
    path('service', views.service)
]
