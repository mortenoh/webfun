
from django.http import HttpResponse
from django.shortcuts import render_to_response

def index(request):
	return render_to_response('calc/index.html', locals())

def eval_view(request):
	if request.method == 'POST':
		from math import *

		try:
			result = eval(request.POST['text'], {"__builtins__":None}, 
							{'e':e, 'pi':pi, 'cos':cos, 
							 'sin':sin, 'tan':tan, 'sqrt':sqrt,
							 'abs':abs})
		except NameError as e:
			result = '<span style="color: #f00;">%s</span>' % e

		return HttpResponse("eval('%s') = %s" % (
			request.POST['text'], result))

	return HttpResponse("Uhm... you should post something.")

