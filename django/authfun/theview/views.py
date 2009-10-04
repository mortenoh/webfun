
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from forms import *

def index(request):

	return render_to_response('index.html', locals())

def login_view(request):
	if request.GET.has_key('next'):
		next = request.GET['next']
	else:
		next = '/secret'

	if request.user.is_authenticated():
		return HttpResponseRedirect('/secret')
	elif request.method == 'POST':
		lf = LoginForm(request.POST)
		if lf.is_valid():
			lf = lf.cleaned_data
			user = authenticate(username=lf['username'], password=lf['password'])

			if user is None:
				return HttpResponseRedirect('/')

			login(request, user)
			return HttpResponseRedirect(next)

	lf = LoginForm()
	return render_to_response('login.html', locals())

def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')

@login_required
def secret(request):
	return render_to_response('secret.html', locals())

