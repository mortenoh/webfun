
from django.http import HttpResponse
from django.shortcuts import render_to_response
from models import Student

def index(request):
	return render_to_response('students/index.html', locals())

def count(request):
	n = Student.objects.all().count();
	return HttpResponse(n, mimetype="text/plain")

