from django.conf import settings
from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth import views

from board import views

urlpatterns = [
    url(r'^boardlist/$',views.Boardlistview.as_view(),name='boardlist'),
    url(r'^(?P<pk>\d+)/$',views.BoardDetailview.as_view(),name = 'detailboard'),
    url(r'^boardwrite/$',views.boardwirte,name='boardwrite')
]