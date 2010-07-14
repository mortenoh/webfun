
from django.template import Template, Context
from django.shortcuts import render_to_response

def index(request):
	page = { 
		'title' : 'index',
		'content' : 'bla bla',
	}

	number_list = [1, 2, 3, 4, 5, 6, 7, 8]

	c = Context({'page': page, 'number_list': number_list})

	return render_to_response('index.html', c)

