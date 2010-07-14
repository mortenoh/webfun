
from django.http import HttpResponse

def index(request):
	return HttpResponse('index.')

def index2(request, n):
	return HttpResponse('index %d' % (int(n)))

