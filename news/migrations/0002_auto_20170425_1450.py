# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-25 11:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='title_news',
            field=models.CharField(max_length=200, verbose_name='Название новости'),
        ),
    ]