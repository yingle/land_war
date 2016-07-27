from django.conf.urls import patterns, include, url
from . import views

urlpatterns = [

    url(r'^$', views.index, name='index'),

    url(r'^(?P<photo_id>[0-9]+)/$', views.detail, name='detail'),

    url(r'^winningest/$', views.winningest, name='winningest'),

    url(r'^losingest/$', views.losingest, name='losingest'),

    url(r'^daily_photo/$', views.daily_photo, name='daily_photo'),

    url(r'^add/$', views.add_photo, name='add'),

    url(r'^rank/$', views.rank, name='rank'),

    url(r'^all_photos/$', views.all_photos, name='all_photos'),

    url(r'^statistic/$', views.statistic, name='statistic'),

]