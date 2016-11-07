from django.conf.urls import url, include
from django.contrib import admin
# from django.views.generic import TemplateView
from django.contrib.auth import views as django_views

from . import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.post_list, name='post_list'),
    url(r'^login/$', django_views.login, {'template_name': 'data_app/login.html'}, name='login'),
    url(r'^logout/$', django_views.logout, {'next_page': '/'}, name='logout'),

    url(r'^post_error/(?P<err>[^/]+)/$', views.post_error, name='post_error'),

    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/(?P<pk>[0-9]+)/remove/$', views.post_remove, name='post_remove'),
]
