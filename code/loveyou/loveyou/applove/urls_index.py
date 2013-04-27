
from django.conf.urls import patterns,include,url
from loveyou.applove.views_regist import *
urlpatterns = patterns('loveyou.applove.views_index',
    url(r'myperson/$','index_myperson',name='myperson_myperson'),
    url(r'mydate/$','index_mydate',name='myperson_mydate'),
    url(r'myfollow/$','index_myfollow',name='myperson_myfollow'),
	url(r'mycollect/$','index_mycollect',name='myperson_collect'),
	url(r'jia/$','index_jia',name='myperson_jia'),
	)

