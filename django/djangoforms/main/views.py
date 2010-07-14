
from django.http import HttpResponse
from django.shortcuts import render_to_response
from forms import *

def index(request):
	if request.method == 'POST':
		blogform = BlogForm(request.POST)
		if blogform.is_valid():
			return HttpResponse('Success.')
	else:
		blogform = BlogForm()

	return render_to_response('index.html', locals())

