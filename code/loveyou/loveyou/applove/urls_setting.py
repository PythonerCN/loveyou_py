from django.conf.urls import patterns, include, url 

urlpatterns = patterns('loveyou.applove.views_setting',
                url(r'^1/$', 'info', name='setting-info'),
                url(r'^2/$', 'password', name='setting-password'),
                url(r'^3/$', 'set_headimg', name='setting-headimg'),
                url(r'^login/$', 'login'),
            ) 

                                                                               
                                   
