
from django.utils.translation import ugettext as _
from django.shortcuts import render_to_response
from django.http import HttpResponse

def index(request):
	return render_to_response('index.html', locals())

