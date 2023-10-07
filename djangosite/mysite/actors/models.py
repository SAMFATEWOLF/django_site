from datetime import date, datetime

from django.db import models
from django.urls import reverse


class Actors(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='URL')
    sex = models.CharField(max_length=100, verbose_name='Пол')
    birth = models.DateField(blank=True, verbose_name='Дата рождения')
    death = models.DateField(blank=True, null=True, verbose_name='Дата смерти')
    bio = models.TextField(blank=True, verbose_name='Биография')
    photo = models.ImageField(upload_to='photos%Y/%m/%d/', verbose_name='Фото')
    crt_time = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    upd_time = models.DateTimeField(auto_now=True, verbose_name='Время обновления')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория', null=True)

    def __str__(self):
        return self.title

    def get_age(self):
        b_s = str(self.birth)
        date_format = '%Y-%m-%d'
        if self.death is None:
            temp = datetime.today() - datetime.strptime(b_s, date_format)
        else:
            d_s = str(self.death)
            temp = datetime.strptime(d_s, date_format) - datetime.strptime(b_s, date_format)
        return temp.days // 365

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'актёров'
        verbose_name_plural = 'Актёры'
        ordering = ['-crt_time', 'title']


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Категория")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})

    class Meta:
        verbose_name = 'категорию'
        verbose_name_plural = 'Категории'
        ordering = ['id']

