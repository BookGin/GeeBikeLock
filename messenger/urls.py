from django.conf.urls import url, include
from django.contrib import admin
from web import views as web_views
from .views import *
urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^create_channel$', create_channel, name='create_channel'),
    url(r'^remove_channel$', remove_channel, name='remove_channel'),
    url(r'^post/$', post, name='post'),
    url(r'^(?P<channel_id>[0-9]+)/$', channel_message, name='channel_message'),
    url(r'^(?P<channel_id>[0-9]+)/post/$', channel_post, name='channel_post'),
    url(r'^upload$', upload_file, name='upload_file'),
    url(r'^uploads/(?P<file_id>[\.a-zA-Z0-9]+)/$', get_file, name='get_file')
]
