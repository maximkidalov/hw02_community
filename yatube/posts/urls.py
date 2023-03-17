from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('groups/', views.groups, name='groups'),
    path('group/<slug:slug>/', views.group_posts, name='group_list'),
    path('user/<int:num>/', views.user_show, name='user_show')
]
