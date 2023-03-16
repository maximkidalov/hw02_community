from django.shortcuts import render
# Импортируем модель, чтобы обратиться к ней
from .models import Post, Group
from django.shortcuts import render, get_object_or_404


def index(request):
    text = 'Это главная страница проекта YaTube'
    posts = Post.objects.order_by('-pub_date')[:10]
    template = ('posts/index.html')
    # В словаре context отправляем информацию в шаблон
    context = {
        'posts': posts,
        'text': text,
    }
    return render(request, template, context)


def group_posts(request, slug):
    # Функция get_object_or_404 получает по заданным критериям объект 
    # из базы данных или возвращает сообщение об ошибке, если объект не найден.
    # В нашем случае в переменную group будут переданы объекты модели Group,
    # поле slug у которых соответствует значению slug в запросе
    group = get_object_or_404(Group, slug=slug)
    template = ('posts/group_list.html')

    # Метод .filter позволяет ограничить поиск по критериям.
    # Это аналог добавления
    # условия WHERE group_id = {group_id}
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    title = 'Лев толстой - зеркало русской революции'
    context = {
        'group': group,
        'posts': posts,
        'title': title,
        'text': 'Здесь будет информация о группах проекта YaTube'
    }
    return render(request, template, context)

# def index(request):
#     template = ('/Users/mufaka/Desktop/Dev/yatube/yatube_project/yatube/'
#                 'templates/posts/index.html')
#     title = "Это главная страница проекта Yatube"
#     text = "Главная страница"
#     context = {
#         'title': title,
#         'text': text,
#     }
#     return render(request, template, context)


# def group_posts(request):
#     template = ('/Users/mufaka/Desktop/Dev/yatube/yatube_project/yatube/'
#                 'templates/posts/group_list.html')
#     title = "Здесь будет информация о группах проекта Yatube"
#     text = "Вложенная страница"
#     context = {
#         'title': title,
#         'text': text,
#     }
#     return render(request, template, context)
