#-*- coding:utf8 -*-
'''个人配置 '''
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from django import forms
from loveyou.applove.models import *
from django.contrib.auth import authenticate
from django.contrib import auth
import time
import random
class SettingInfo(forms.Form):
    ''' 个人信息表单 '''
    firstname = forms.CharField(label='昵称')
    email = forms.EmailField(label='邮箱')
def info(request):
    ''' 个人信息 '''
    if request.method == 'POST':
        settinginfo = SettingInfo(request.POST)
        if settinginfo.is_valid():
            firstname = settinginfo.cleaned_data['firstname']
            email = settinginfo.cleaned_data['email']
            user = request.user
            user.email = email
            user.first_name = firstname
            user.save()
            return HttpResponseRedirect('/setting/1/')
    else:
        users = User.objects.exclude(username__exact=request.user.username).exclude(username='root')

        settinginfo = SettingInfo()
    return render_to_response('setting_info.html', {'settinginfo':settinginfo, 'request':request})
class PasswordForm(forms.Form):
    oldpassword = forms.CharField(widget=forms.PasswordInput,
                                    label='输入旧密码')
    newpassword1 = forms.CharField(widget=forms.PasswordInput,
                                    label='输入新密码')
    newpassword2 = forms.CharField(widget=forms.PasswordInput,
                                    label='确认新密码')
    def clean_newpassword2(self):
        ''' 验证新密码'''
        if 'newpassword1' in self.cleaned_data:
            newpassword1 = self.cleaned_data['newpassword1']
            newpassword2 = self.cleaned_data['newpassword2']
            if newpassword1 == newpassword2:
                return newpassword2
        raise forms.ValidationError('两次密码不一致')

def password(request):
    ''' 密码 '''
    if request.method == 'POST':
        passwordform = PasswordForm(request.POST)
        if passwordform.is_valid():
            opassword = passwordform.cleaned_data['oldpassword']
            if authenticate(username=request.user.username, password=opassword):
                password = passwordform.cleaned_data['newpassword2']
                user = request.user
                user.set_password(password)
                user.save()
            else:
                return HttpResponse('原始密码不正确')
            auth.logout(request)
            return HttpResponseRedirect('/login/login/')
    else:
        passwordform = PasswordForm()
    return render_to_response('setting_password.html',{'passwordform':passwordform, 'request':request})
class HeadimgForm(forms.Form):
    ''' 头像表单 '''
    headimg = forms.FileField(label='头像')
def set_headimg(request):
    ''' 头像 '''
    if request.method == 'POST':
        headimgform = HeadimgForm(request.POST,request.FILES)
        if headimgform.is_valid():
            headimg = headimgform.cleaned_data['headimg']
            headimg_name = time.strftime("%Y%m%d%H%M%S",time.localtime())
            headimg._set_name(headimg_name)
            name =request.user.get_profile()
            name.headimg = headimg
            name.save()
    else:
        headimgform = HeadimgForm()
    return render_to_response('setting_headimg.html', {'headimgform':headimgform, 'request':request})

def login(request):
    return render_to_response('login.html', {})

