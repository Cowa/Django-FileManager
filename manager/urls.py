from django.conf.urls import patterns, url

from manager import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<folder_id>\d+)/$', views.test, name='test')
)
