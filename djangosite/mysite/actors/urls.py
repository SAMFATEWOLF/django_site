from django.contrib import admin
from django.urls import path, include

from actors.views import *

urlpatterns = [
    path('', ActorsHome.as_view(), name='home'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('about/', about, name='about'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('category/<int:cat_id>/', ShowCategory.as_view(), name='category'),
    path('register/', RegisterUser.as_view(), name='register')
]
