from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.core.paginator import Paginator

from .models import Post, Group


def index(request):
    """Метод вывода главной страницы"""
    template = 'posts/index.html'
    posts = Post.objects.select_related('group', 'author')
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    pagination = paginator.get_page(page_number)
    context = {'items': pagination}
    return render(request, template, context)


def group_posts(request, slug):
    """Метод для вывода списка записей от группы"""
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    post = group.posts.select_related('author', 'group')
    paginator = Paginator(post, 10)
    page_number = request.GET.get('page')
    pagination = paginator.get_page(page_number)
    context = {'group': group,
               'items': pagination
               }
    return render(request, template, context)


def groups(request):
    """Метод для вывода списка групп."""
    template = 'posts/groups.html'
    groups = Group.objects.all()
    paginator = Paginator(groups, 25)
    page_number = request.GET.get('page')
    pagination = paginator.get_page(page_number)
    context = {'items': pagination}
    return render(request, template, context)


def user_show(request, num):
    """Метод для вывода информации про автора."""
    template = 'posts/user.html'
    user = get_object_or_404(User, id=num)
    author = Post.objects.all().filter(author=user).count()
    context = {'user': user,
               'count': author
               }

    return render(request, template, context)


def page_not_found_view(request, exception):
    """Метод для вывода отдельной страницы c ошибкой."""
    return render(request, '404.html', status=404)
