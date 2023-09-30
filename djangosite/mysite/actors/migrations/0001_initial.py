# Generated by Django 4.2.5 on 2023-09-28 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='URL')),
                ('sex', models.CharField(max_length=100, verbose_name='Пол')),
                ('birth', models.DateField(blank=True, verbose_name='Дата рождения')),
                ('death', models.DateField(blank=True, null=True, verbose_name='Дата смерти')),
                ('bio', models.TextField(blank=True, verbose_name='Биография')),
                ('photo', models.ImageField(upload_to='protos%Y/%m/%d/', verbose_name='Фото')),
                ('crt_time', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('upd_time', models.DateTimeField(auto_now=True, verbose_name='Время обновления')),
                ('is_published', models.BooleanField(default=True, verbose_name='Публикация')),
            ],
        ),
    ]