from django.shortcuts import render_to_response
from django.http import HttpResponse , HttpResponseRedirect
def love(request):
    s = []
    return render_to_response('index.html',{'s':s})
