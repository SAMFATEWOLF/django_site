# Generated by Django 4.2.5 on 2023-10-09 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('actors', '0004_alter_actors_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actors',
            name='cat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='actors.category', verbose_name='Категория'),
        ),
    ]
