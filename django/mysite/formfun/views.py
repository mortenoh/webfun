
from django.http import HttpResponse
from django.shortcuts import render_to_response

def form1(request):
    values = request.META.items() 
    values.sort() 
    html = [] 
    for k, v in values: 
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v)) 

    return HttpResponse('<table border="1">%s</table>' % '\n'.join(html)) 

def form2(request):
	return render_to_response('formfun/search_form.html')

def search(request):
	if 'q' in request.GET:
		message = 'You searched for: %r.' % request.GET['q']
	else:
		message = 'You submitted an empty form.'

	return HttpResponse(message)

