# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

from traning_product import settings
from  . import views
urlpatterns = [
    url(r'^articles/', views.list_article, name='article'),
    url(r'^article/(?P<pk>\d+)/$', views.article_detail, name='article_det')
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns() + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)