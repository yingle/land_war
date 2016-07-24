from django.conf.urls import patterns, include, url
from . import views

urlpatterns = [

    url(r'^$', views.index, name='index'),

    url(r'^winningest/$', views.winningest, name='winningest'),

    url(r'^losingest/$', views.losingest, name='losingest'),

    url(r'^add/$', views.add_photo, name='add'),

    url(r'^all_photos/$', views.all_photos, name='all_photos'),

]