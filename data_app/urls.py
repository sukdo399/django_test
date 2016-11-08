from django.conf.urls import url, include
from django.contrib import admin
# from django.views.generic import TemplateView
from django.contrib.auth import views as django_views
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

# router = routers.DefaultRouter()
# router.register(r'posts', views.RestPostViewSet)

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

    url(r'^rest-api/post-list/$', views.RestPostList.as_view()),
    url(r'^rest-api/post-list/(?P<pk>[0-9]+)/$', views.RestPostDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)


"""
curl -H 'Accept: application/json; indent=4' -u USER:PASSWORD http://127.0.0.1:8000/rest-api/post-list/
http -a USER:PASSWORD http://127.0.0.1:8000/rest-api/post-list/

curl -X post -H 'Accept: application/json; indent=4' -u USER:PASSWORD -F "file=@/home/shko/work/python/2016-10-14.xlsx" -F "author=1" http://127.0.0.1:8000/rest-api/post-list/
curl -X post -H 'Accept: application/json; indent=4' -u USER:PASSWORD -F "file=@/home/shko/work/python/2016-10-14.xlsx" http://127.0.0.1:8000/rest-api/post-list/

"""
