from django import template
from django.db.models import Count

from actors.models import *

register = template.Library()


@register.simple_tag()
def get_categories(filter=None):
    if not filter:
        return Category.objects.all()
    else:
        return Category.objects.filter(pk=filter)


@register.inclusion_tag('actors/list_categories.html')
def show_categories(sort=None, cat_selected=0):
    if not sort:
        cats = Category.objects.annotate(Count('actors'))
    else:
        cats = Category.objects.annotate(Count('actors')).order_by(sort)

    return {'cats': cats, 'cat_selected': cat_selected}
