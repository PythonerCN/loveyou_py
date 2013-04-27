from django.conf.urls import patterns, include, url

urlpatterns = patterns('loveyou.applove.views_myhome',
    url(r'^myhome/$', 'myhome', name='myhome_myhome'),

)

