from django.shortcuts import render, get_object_or_404
from .models import Post, Group

MESSAGES = 10  # Количество выводимых новых сообщений
# https://i.postimg.cc/k5hwXXk0/WM-Screenshots-20230323172837.png


def index(request):
    posts = Post.objects.order_by('-pub_date')[:MESSAGES]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_list(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:MESSAGES]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
