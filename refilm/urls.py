from django.conf.urls import url, include, patterns
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from django.views.generic import TemplateView

from . import views

urlpatterns = patterns('',
                       url(r'^$', views.movie_embed, name="index"),
                       )