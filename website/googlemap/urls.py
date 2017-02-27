from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^unlock/(?P<bike_id>[0-9a-zA-Z]+)/$',  views.unlock,  name='unlock'),
    url(r'^remove/(?P<bike_id>[0-9a-zA-Z]+)/$',  views.remove,  name='remove'),
    url(r'^lock/(?P<bike_id>[0-9a-zA-Z]+)/$',  views.lock,  name='lock'),
    url(r'^list',  views.list,  name='list'),
    url(r'^register_bike',  views.register_bike,  name='register_bike'),
    url(r'^(?P<bike_id>[0-9a-zA-Z]+)/$', views.update, name='update'),
]
