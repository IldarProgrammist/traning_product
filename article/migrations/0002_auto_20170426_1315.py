# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-26 10:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images_article',
            name='title_photo',
            field=models.CharField(max_length=200, verbose_name='Название картики'),
        ),
    ]
