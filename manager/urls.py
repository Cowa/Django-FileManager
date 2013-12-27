from django.conf.urls import patterns, url

from manager import views

urlpatterns = patterns('',
    # URL pattern : adress/, root
    url(r'^$', views.index, name='index'),
    # URL pattern : address/4, where 4 is a folder's id
    url(r'^(?P<folder_id>\d+)/$', views.folder, name='folder')
)
