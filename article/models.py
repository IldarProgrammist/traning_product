# -- encoding: utf-8 --
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название поста')
    text_post = RichTextUploadingField(blank=True, default='')
    created = models.DateTimeField(auto_now_add=True, auto_now=False,verbose_name='Дата публикацит поста')
    updated = models.DateTimeField(auto_now_add=False, auto_now=True,verbose_name='Дата обновления поста')


    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = 'Посты'


    def get_absolute_url(self):
        return reverse("article_det", args=[str(self.id)])


#Картинки для постов
class Images_Article(models.Model):
    title_photo = models.CharField(max_length=200, verbose_name='Название картики')
    slug = models.ForeignKey(Article)
    image = models.ImageField(verbose_name='картинка', blank=True)

    def __str__(self):
        return self.title_photo

    class Meta:
        verbose_name = "Картинка"
        verbose_name_plural = 'Картинки'

class Comment(models.Model):
    comments_text = models.TextField()
    ccomments_article = models.ForeignKey(Article)


