from django.urls import path
from . import views

# path('test', views.test) : 주소, 그 주소로 가면 사용되는 함수 명

urlpatterns = [
    path('', views.index),
    
    path('list/', views.list, name='list'),
    path('addpost/', views.AddPost.as_view(), name='addpost'),
    path('<int:pk>/detail/', views.detail, name='detail'),
    
#     path('<int:pk>/edit/', views.PostEditView.as_view(), name='edit'),

    
    path('login/', views.LoginView.as_view(), name='login'),
]
