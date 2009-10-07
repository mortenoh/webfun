
from django.http import HttpResponse
from django.shortcuts import render_to_response

from models import Student
import json

def index(request):
	return render_to_response('students/index.html', locals())

def count_plaintext(request):
	n = Student.objects.all().count();
	return HttpResponse(n, mimetype="text/plain")

def count_json(request):
	n = {'count' : Student.objects.all().count()}
	return HttpResponse(json.dumps(n), mimetype="application/json")

def count_xml(request):
	n = '<count>%s</count>' % (Student.objects.all().count())
	return HttpResponse(n, mimetype="application/xml")

