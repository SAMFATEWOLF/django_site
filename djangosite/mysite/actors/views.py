from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import *
from .models import *
from .utils import *


class ActorsHome(DataMixin, ListView):
    model = Actors
    template_name = 'actors/startpage.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        return dict(list(context.items()) + list(c_def.items()))

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


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'actors/addpage.html'
    login_url = reverse_lazy('admin')  # TODO: отправить на авторизацию, вернуть через утилс

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавление статьи')
        return dict(list(context.items()) + list(c_def.items()))


class ShowPost(DataMixin, DetailView):
    model = Actors
    template_name = 'actors/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        return dict(list(context.items()) + list(c_def.items()))


class ShowCategory(DataMixin, ListView):
    model = Actors
    template_name = 'actors/startpage.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Actors.objects.filter(cat__id=self.kwargs['cat_id'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Категория - ' + str(context['posts'][0].cat),
                                      cat_selected=context['posts'][0].cat_id)
        return dict(list(context.items()) + list(c_def.items()))
