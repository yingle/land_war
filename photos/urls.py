from django.conf.urls import patterns, include, url
from . import views

urlpatterns = [

    url(r'^$', views.index, name='index'),

    url(r'^winningest/$', views.winningest, name='winningest'),

    url(r'^losingest/$', views.losingest, name='losingest'),

]