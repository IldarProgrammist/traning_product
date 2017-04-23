# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-23 06:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название поста')),
                ('text_post', models.TextField(verbose_name='Текст поста')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикацит поста')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата обновления поста')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
            },
        ),
    ]