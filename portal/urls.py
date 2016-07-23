from django.conf.urls import url
from . import views

urlpatterns = [
    # ex: /portal/
    url(r'^$', views.personal_space, name='personal_space'),
]