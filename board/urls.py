from django.conf import settings
from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth import views

from board.views import boardlist

urlpatterns = [
    url(r'^',boardlist,name='boardlist'),
]