from django.http import HttpResponse
from django import forms
from loveyou.applove.models import Sort,YuiHui
class CreateForm(forms.ModelForm):
	class Meta:
	model = Sort
	fields = ('user','city','type','time','sexs')
def create(request):
	if request.method == 'POST':
		createform = CreateForm(request.POST)
		if createform.is_valid():
			user = createform.cleaned_data['user']
			city = createform.cleaned_data['city']
			type = createform.cleaned_data['type']
			time = createform.cleaned_data['time']
			sexs = createform.cleaned_data['sexs']
			sort = Sort.objects.create(user='user',city='city',type='type',time='time',sexs='sexs')
			return HttpResponse('aa')
	else:
		createform = CreateForm()
	return render_to_response('create.html',{'createform':createform})



