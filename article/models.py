# -- encoding: utf-8 --
from django.db import models
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название поста')
    text_post = models.TextField(verbose_name='Текст поста')
    created = models.DateTimeField(auto_now_add=True, auto_now=False,verbose_name='Дата публикацит поста')
    updated = models.DateTimeField(auto_now_add=False, auto_now=True,verbose_name='Дата обновления поста')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = 'Посты'

    def get_absolute_url(self):
        return reverse("article_det", args=[str(self.id)])