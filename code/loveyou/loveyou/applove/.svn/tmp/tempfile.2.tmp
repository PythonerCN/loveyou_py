'''views_regist.py'''
#coding:utf8
from django.contrib.auth import authenticate , login , logout
from django.http import HttpResponse , HttpResponseRedirect
from django import forms
from django.shortcuts import render_to_response
from loveyou.applove.models import *
from django.contrib.auth.models import User
import re

choices_sexs = (
    ('male',u'男'),
    ('female',u'女'),
)
choices_citys = (('shanghai','shanghai'),('tianjin','tianjin'), ('beijing','beijing'),('shijiazhuang','shijiazhuang'),('qinhuangdao','qinhuangdao'),)

users = User.objects.all()
def validate(value):
    '''验证用户'''
    for user in users:
        if value == user.username:
            raise forms.ValidationError("用户名已存在")
def validator(value):
    '''验证密码'''
    pp = re.compile("\w")
    pa = pp.match(value)
    if pa is None:
        raise forms.ValidationError("密码以数字，字母，下划线组成")
class RegistForm(forms.Form):	
    '''RegistForm'''
    username = forms.CharField(max_length=16,min_length=6,validators=[validate,validator],label="用户名",error_messages={'required':'请输入帐号'})
    first_name = forms.CharField(max_length=30,label="昵称",error_messages={'required':'请输入昵称'})
    email = forms.EmailField(label="邮箱",error_messages={'required':'邮箱不能为空'})
    password = forms.CharField(widget=forms.PasswordInput,label="密码",error_messages={'required':'密码不能为空'})
    re_password = forms.CharField(widget=forms.PasswordInput,label="确认密码",error_messages={'required':'重复密码不能为空'})
    sex = forms.ChoiceField(choices = choices_sexs,label='性别')
    address = forms.ChoiceField(choices = choices_citys,label='地址')
    headimg = forms.FileField(label="头像")
    def clean_re_password(self):
        '''验证密码'''
        if 'password' in self.cleaned_data:
            password1 = self.cleaned_data['password']
            password2 = self.cleaned_data['re_password']
        if password1 == password2:
            return password2
        raise forms.ValidationError('两次密码不一致')
def regist(request):
    '''regist'''
    if request.method == 'POST':
        registform = RegistForm(request.POST,request.FILES)
        if registform.is_valid():
            username = registform.cleaned_data['username']
            first_name = registform.cleaned_data['first_name']
            email = registform.cleaned_data['email']
            password = registform.cleaned_data['password']
            re_password = registform.cleaned_data['re_password']
            address = registform.cleaned_data['address']
            sex = registform.cleaned_data['sex']
            headimg = registform.cleaned_data['headimg']
            user = User.objects.create_user(
                username,
                email,
                password,
            )
            user.first_name = first_name
            user.save()
            UserProfile.objects.create(headimg=headimg,address=address,sex=sex,user=user)
            return HttpResponseRedirect('/login/login/')
    else:
        registform = RegistForm()
    return render_to_response('register.html',{'registform':registform})



	

