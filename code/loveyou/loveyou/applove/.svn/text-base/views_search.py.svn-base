'''views_search'''
#coding:utf8
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django import forms
import os,random
from loveyou.applove.models import UserProfile,Sort,YueHui
#from django.contrib.auth.decorators import login_required
#@login_required
class SForm(forms.ModelForm):
    '''搜索表单'''
    class Meta:
        model = Sort
        fields = ('city','type','time','sexs')
def search(request):
    user1 = request.user
    user = User.objects.all()
    sort = Sort.objects.all()
    if request.method == 'POST':
        sform = SForm(request.POST)
        if sform.is_valid():
            city = sform.cleaned_data['city']
            type = sform.cleaned_data['type']
            time = sform.cleaned_data['time']
            sexs = sform.cleaned_data['sexs']
            sorts = sort.filter(city=city).filter(type=type).filter(time=time).filter(sexs=sexs)
            return render_to_response('search.html',{'sform':sform,'sorts':sorts,'request':request,'user':user,'user1':user1})
                     
#            user2 = user1.all().filter(type=type)
#            user3 = user2.all().filter(time=time)
#            user4 = user3.all().filter(sexs=sexs)
#            user5 = user4.user.exclude(username=request.user.username).exclude(username='root')
    else:
        sform = SForm()
    return render_to_response('search.html',{'sform':sform,'request':request,'user':user,'user1':user1})
