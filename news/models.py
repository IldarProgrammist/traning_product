# -- encoding: utf-8 --
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.urls import reverse


class News(models.Model):
    title_news = models.CharField(max_length=200, verbose_name='Название новости')
    text_news = RichTextUploadingField(blank=True, default='')
    img_news = models.ImageField()
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Дата публикации новости')
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name='Дата обновления новости')

    def __str__(self):
        return self.text_news

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = 'Новости'

    def get_absolute_url(self):
        return reverse("news_det", args=[str(self.id)])
