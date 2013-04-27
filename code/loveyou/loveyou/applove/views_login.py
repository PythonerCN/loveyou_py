'''login.py'''
#coding:utf8
from django.http import HttpResponse,HttpResponseRedirect
from django import forms
from loveyou.applove.models import UserProfile,YueHui,LiuYan,Sort
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.shortcuts import render_to_response
import models

class LoginForm(forms.Form):
	'''登录表单'''
	name = forms.CharField(max_length=10,label='姓名')
	password = forms.CharField(max_length=12,label='密码',widget=forms.PasswordInput)
def ulogin(request):
	'''登录'''
	if request.method == 'POST':
		loginform = LoginForm(request.POST)
		if loginform.is_valid():
			name = loginform.cleaned_data['name']
			password = loginform.cleaned_data['password']
			user = authenticate(username=name,password=password)
			if user is not None:
				if user.is_active:
					login(request,user)
					return HttpResponseRedirect('/home/myperson')
		else:
			return HttpResponse('用户名或密码错误')
	else:
		loginform = LoginForm()
	return render_to_response('login.html',{'loginform':loginform})










