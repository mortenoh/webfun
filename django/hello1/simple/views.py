
from django.http import HttpResponse
from django.shortcuts import render_to_response

def t(request):
	person = {'name' : "Morten Olav Hansen", 'age' : 29}
	persons = ['Morten', 'Olav', 'Hansen']

	b1 = True
	b2 = False
	name = 'Morten Olav Hansen'
	return render_to_response('index.html', locals())

def index(request, n):
	return HttpResponse("N = %d" % int(n))
