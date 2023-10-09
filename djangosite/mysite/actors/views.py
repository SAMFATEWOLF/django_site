from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView

from .forms import *
from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'},
        ]


class ActorsHome(ListView):
    model = Actors
    template_name = 'actors/startpage.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Главная страница'
        context['cat_selected'] = 0
        return context

    def get_queryset(self):
        return Actors.objects.filter(is_published=True)


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


class AddPage(CreateView):
    form_class = AddPostForm
    template_name = 'actors/addpage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Добавление статьи'
        return context


class ShowPost(DetailView):
    model = Actors
    template_name = 'actors/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Статья - ' + str(context['post'])
        return context


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
