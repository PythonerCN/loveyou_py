#coding:utf8
from django.conf.urls import patterns, include, url
import os
from loveyou.applove.views_index import *
from loveyou.applove import *
from django.contrib import admin
admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'loveyou.views.home', name='home'),
    # url(r'^loveyou/', include('loveyou.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'js/(?P<path>.*)$', 'django.views.static.serve',{'document_root':os.path.join(os.path.dirname(__file__),"./templates/js")},name='js'),
    url(r'css/(?P<path>[\w\.\-]+\.css)$', 'django.views.static.serve',{'document_root':os.path.join(os.path.dirname(__file__),"./templates/css")},name='css'),
    url(r'img/(?P<path>[\w\.\-]+\.*)$', 'django.views.static.serve',{'document_root':os.path.join(os.path.dirname(__file__),"./templates/img")},name='img'),

    url(r'media/(?P<path>[\w\.\-]+\.*)$', 'django.views.static.serve',{'document_root':os.path.join(os.path.dirname(__file__),"./mymedia")},name='media'),
)
urlpatterns += patterns('',
    url(r'^$', 'loveyou.applove.views.love'),
    url(r'^index/', 'loveyou.applove.views.love'),
    url(r'^home/', include('loveyou.applove.urls_index')),
    url(r'^regist/', include('loveyou.applove.urls_regist')),#郝伟博
    url(r'^search/', include('loveyou.applove.urls_search')),
    url(r'^login/',include('loveyou.applove.urls_login')),
    url(r'^gc/',include('loveyou.applove.urls_gc')),#yangzhiyu
    url(r'^setting/',include('loveyou.applove.urls_setting')),#yangzhiyu
	#url(r'^public/',include('loveyou.applove.urls_public')),
	)
