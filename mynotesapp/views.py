from django.shortcuts import render
from mynotesapp.models import Note , Note1,Note2
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'home.html')
             
@login_required	
def exer(request):
    context ={
	'notes': Note.objects.filter(),
    'note1': Note1.objects.filter(),
    'note2': Note2.objects.filter()
	}
    return render(request, 'service.html',context)