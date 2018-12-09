from django.urls import re_path

from . import views

app_name = 'contentapp'

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.detail_content, name='detail_content'),
    re_path(r'^edit/(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.edit_content, name='edit_content'),
    re_path(r'^delete/(?P<id>\d+)/$', views.delete_content, name='delete_content'),
    re_path(r'^upload/$', views.upload_content, name='upload_content'),
    re_path(r'^share/$', views.share_insta_content, name='share_insta_content'),
]
