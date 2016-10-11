from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'u/(?P<streamer_name>[a-zA-Z0-9_]+)/$', views.detail, name='detail'),
    url(r'about/$', views.about, name='about'),
]
