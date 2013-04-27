#coding:utf8
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from loveyou.applove.models import *
def index_myperson(request):
    user = request.user
    print user
    context = {'user':user}
    return render_to_response('index_myperson.html',context)
def index_mydate(request):
    user = request.user
    yuehui = user.yuehui_set.all()
    context = {'user':user,'yuehui':yuehui}
    return render_to_response('index_mydate.html',context)

def index_myfollow(request):
    '''关注'''
    user = request.user
    context = {'user':user}
    return render_to_response('index_myfollow.html',context)
def index_mycollect(request):
    '''收藏'''
    user = request.user
    user1 = user.get_profile()
    collect_num = len(user1.collect.all())
#    collect_num = len(user.userprofile.collect.all())
    collect = user1.collect.all()
    context = {'user':user,'collect_num':collect_num,'collect':collect}
    return render_to_response('index_mycollect.html',context)











