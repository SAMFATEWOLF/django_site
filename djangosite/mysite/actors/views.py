from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404, redirect

from .forms import *
from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'},
        ]


def start_page(request):
    posts = Actors.objects.all()

    context = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': posts,
        'cat_selected': 0,

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
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddPostForm()
    return render(request, 'actors/addpage.html', {'form': form, 'menu': menu, 'title': 'Добавление статьи'})


def show_post(request, post_slug):
    post = get_object_or_404(Actors, slug=post_slug)

    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': post.cat_id,

    }
    return render(request, 'actors/post.html', context=context)


def show_category(request, cat_id):
    posts = Actors.objects.filter(cat_id=cat_id)

    if len(posts) == 0:
        raise Http404()

    context = {
        'title': 'Отображение по рубрикам',
        'menu': menu,
        'posts': posts,
        'cat_selected': cat_id,

    }

    return render(request, 'actors/startpage.html', context=context)
