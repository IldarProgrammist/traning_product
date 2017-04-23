# -*- coding: utf-8 -*-
from django.conf.urls import url
from  . import views
urlpatterns = [
    url(r'^articles/', views.list_article, name='article'),
    url(r'^article/(?P<pk>\d+)/$', views.article_detail, name='article_det')
]