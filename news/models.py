# -- encoding: utf-8 --
from django.db import models
from django.urls import reverse


class News(models.Model):
    title_news = models.CharField(max_length=100)
    text_news = models.TextField()
    img_news = models.ImageField()
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Дата публикацит поста')
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name='Дата обновления поста')


    def __str__(self):
        return self.title_news

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = 'Новости'

    def get_absolute_url(self):
        return reverse("article_det", args=[str(self.id)])