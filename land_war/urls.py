from django.conf.urls import include, url
from django.contrib import admin
from . import views


urlpatterns = [
    # Examples:
    # url(r'^$', 'landscape_war.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^photos/', include('photos.urls')),

    url(r'^$', views.main_page),

    url(r'^portal/$', include('portal.urls', namespace="portal")),

    url(r'^logout/$', views.logout_view, name='logout_view'),

    url(r'^', include('django.contrib.auth.urls')),

    url(r'^admin/', include(admin.site.urls)),
]