from django.contrib import admin
from django.urls import path, include

from actors.views import *

urlpatterns = [
    path('', start_page, name='home'),
    path('post/<int:post_id>/', show_post, name='post'),
    path('about/', about, name='about'),
    path('addpage/', addpage, name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('category/<int:cat_id>/', show_category, name='category')
]
