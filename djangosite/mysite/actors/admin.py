from django.contrib import admin
from .models import *


class ActorsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'crt_time', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'bio')
    list_editable = ('is_published',)
    list_filter = ('crt_time', 'title', 'is_published')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('id', 'name')
    search_fields = ('name',)


admin.site.register(Actors, ActorsAdmin)
admin.site.register(Category, CategoryAdmin)

# Register your models here.
