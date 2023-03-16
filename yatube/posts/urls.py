from django.urls import path
from . import views

app_name = 'yatube'

urlpatterns = [
    # path('', views.index),
    # path('group_list.html', views.group_posts)
    path('', views.index, name='index'),
    path('group/<slug>/', views.group_posts, name='group_list'),
]
