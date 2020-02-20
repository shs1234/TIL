from django.urls import path
from . import views

# path('test', views.test) : 주소, 그 주소로 가면 사용되는 함수 명

app_name='myboard'
urlpatterns = [
    path('<category>/<int:pk>/<mode>/', views.BoardView.as_view(), name='myboard'),

]