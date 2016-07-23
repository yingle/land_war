from django.conf.urls import patterns, include, url
from . import views

urlpatterns = [

    url(r'^$', views.registration_view, name='registration_view'),

]