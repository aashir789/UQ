from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'UQ.views.home', name='home'),
    url(r'^playLink', 'UQ.views.playLink', name='playLink'),
)
