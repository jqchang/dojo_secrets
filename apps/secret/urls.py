from django.conf.urls import url, include
from . import views
# from django.contrib import admin

urlpatterns = [
    url(r'^$', views.index, name='secret_index'),
    url(r'^process$', views.process, name='secret_process'),
    url(r'^popular$', views.popular, name='secret_popular'),
    url(r'^delete/(?P<id>\d+)$', views.delete, name='secret_delete'),
    url(r'^like/(?P<message_id>\d+)$', views.like, name='secret_like')
]
