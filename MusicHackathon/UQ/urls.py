from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'UQ.views.home', name='home'),
    url(r'^playLink', 'UQ.views.playLink', name='playLink'),
    url(r'^getVID', 'UQ.views.getVID', name='getVID'),
    url(r'^upVote/(?P<id>\d+)$', 'UQ.views.upVote', name='upVote'),
    url(r'^downVote/(?P<id>\d+)$', 'UQ.views.downVote', name='downVote'),
    url(r'^login$', 'django.contrib.auth.views.login', {'template_name':'UQ/login.html'}, name='login'),
    url(r'^logout$', 'django.contrib.auth.views.logout_then_login', name='logout'),
)
