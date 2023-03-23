from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    #  Главная страница
    path('', views.index),
    #  Группа
    path('group/<slug:slug>/', views.group_list, name='group_list'),
]
