from django.contrib import admin
from django.urls import path, include

from actors.views import *

urlpatterns = [
    path('', ActorsHome.as_view(), name='home'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('about/', about, name='about'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('category/<int:cat_id>/', show_category, name='category')
]
