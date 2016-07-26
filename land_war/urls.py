from django.conf.urls import include, url
from django.contrib import admin
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    # Examples:
    # url(r'^$', 'landscape_war.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^photos/', include('photos.urls', namespace="photos")),

    url(r'^$', views.main_page),

    url(r'^portal/$', include('portal.urls', namespace="portal")),

    url(r'^registration/$', include('registration.urls', namespace="registration")),

    url(r'^logout/$', views.logout_view, name='logout_view'),

    url(r'^', include('django.contrib.auth.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)