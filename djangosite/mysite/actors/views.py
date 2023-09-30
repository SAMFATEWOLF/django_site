from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render
from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'},
        ]


def start_page(request):
    posts = Actors.objects.all()
    cats = Category.objects.all()

    context = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': posts,
        'cat_selected': 0,
        'cats': cats,

    }

    return render(request, 'actors/startpage.html', context=context)


def about(request):
    context = {
        'title': 'О сайте',
        'menu': menu
    }
    return render(request, 'actors/about.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('page not found')


def contact(request):
    return HttpResponse('contact')


def login(request):
    return HttpResponse('login')


def addpage(request):
    return HttpResponse('addpage')


def show_post(request, post_id):
    return HttpResponse(f'post: {post_id}')


def show_category(request, cat_id):
    posts = Actors.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()

    if len(posts) == 0:
        raise Http404()

    context = {
        'title': 'Отображение по рубрикам',
        'menu': menu,
        'posts': posts,
        'cat_selected': cat_id,
        'cats': cats,

    }

    return render(request, 'actors/startpage.html', context=context)
