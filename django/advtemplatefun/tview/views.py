
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

def custom_proc(request):
	return {
		'text' : 'This is some text from a custom processor',
	}

def index(request):
	l = 'ApPlE'

	return render_to_response('index.html', locals(),
			context_instance=RequestContext(request, processors=[custom_proc]))

