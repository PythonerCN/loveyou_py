#coding:utf8
import datetime

from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

choices_sexs = (
    ('male','male'),
    ('female','female'),
)

choices_citys = (
    ('shanghai','shanghai'),('tianjin','tianjin'), ('beijing','beijing'),('shijiazhuang','shijiazhuang'),('qinhuangdao','qinhuangdao'))
#扩展user
class UserProfile(models.Model):
    headimg = models.FileField(upload_to="./")
    address = models.CharField(max_length=20,choices = choices_citys)
    user = models.ForeignKey(User,unique=True)
    sex = models.CharField(max_length = 20,choices = choices_sexs)
    yuehui = models.ManyToManyField('YueHui',verbose_name = "约会", null=True, blank=True)
    collect = models.ManyToManyField('YueHui', verbose_name=u"收藏", related_name='milestone_task', null=True, blank=True)
    follow = models.ManyToManyField(User, verbose_name=u"关注", related_name='milestone_task', null=True, blank=True)
    def __unicode__(self):
        return self.user.username

#分类
choices_type=(
    ('coffee','coffee'),('travel','travel'),('chat','chat'),('hang','hang'),

)
choices_time=(
    ('Mon','Monday'),('Tues','Tues'),('Wed','Wendnesday'),('Thur','Thursday'),('Fri','Friday'),('Sat','Saturday'),('Sun','Sunday'),
)
    

class Sort(models.Model):
    user = models.ForeignKey(User)
    city = models.CharField(max_length=100,choices=choices_citys)
    sexs = models.CharField(max_length = 20,choices = choices_sexs)
    type = models.CharField(max_length = 10,choices = choices_type)
    time = models.CharField(max_length = 10,choices = choices_time)
    def __unicode__(self):
        return self.user.username


#约会类的
class YueHui(models.Model):
    xuser = models.ForeignKey(User)
    sort = models.ManyToManyField(u'Sort')
    content = models.TextField(max_length = 200,verbose_name = '内容',null = True)
    r_time = models.DateTimeField(auto_now=True)#时间
    class Meta:
        ordering = ['-r_time']
    def __unicode__(self):
        return self.content
#留言板
class LiuYan(models.Model):
    renote = models.ForeignKey(User,verbose_name='留言',null = True,blank=True)
    reply = models.TextField(verbose_name = "回复")
#class Personal(models.Model):
#	'''私信 ''' 
#	title = models.CharField(max_length=100)
#	context = models.TextField()
#	p_time  = models.DateTimeField(auto_now=True)
#	shou_user = models.ForeignKey(User)   #收件人
#	fa_user = models.ForeignKey(User,related_name='user_id') #发件人
#	def __unicode__(self):
#		return self.title


