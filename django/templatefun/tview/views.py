
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context, RequestContext
from django.shortcuts import render_to_response

from models import Course
from forms import *

def index(request):
	name = "MORTEN"

	t = get_template('tview/index.html')
	html = t.render(Context(locals()));
	return HttpResponse(html)

def index2(request):
	name = "MORTEN"
	age = 28
	b = True
	l = ['apple','banana','orange','kiwi']

	return render_to_response('tview/index.html', locals())

def model1(request):
	courses = Course.objects.all().order_by("-name")
	return render_to_response('tview/model1.html', locals())

def add(request):
	if request.method == 'POST':
		f = CourseForm(request.POST)

		if f.is_valid():
			fc = f.cleaned_data
			Course.objects.create(name=fc['name'], 
					description=fc['description'])
			return HttpResponseRedirect('/')
		else:
			return render_to_response('tview/add.html', locals())
	else:
		f = CourseForm()
		return render_to_response('tview/add.html', locals())

def view_id(request, cid):
	c = Course.objects.get(id=cid)
	html = c.name + " | " + c.description

	return HttpResponse(html)

