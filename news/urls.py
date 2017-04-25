# -*- coding: utf-8 -*-
from django.conf.urls import url
from  . import views

urlpatterns = [
      url(r'^news/', views.list_news, name='news'),
      url(r'^new/(?P<pk>\d+)/$', views.news_detail, name='news_det')]