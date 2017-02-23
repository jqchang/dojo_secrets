from django.conf.urls import url, include
from . import views
# from django.contrib import admin

urlpatterns = [
    url(r'^$', views.index, name='login_index'),
    # url(r'^success$', views.success, name='login_success'),
    url(r'^process$', views.process, name='login_process'),
    url(r'^login$', views.login, name='login_login'),
    url(r'^logout$', views.logout, name='login_logout')
]
