
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from forms import LoginForm

def index(request):
	return render_to_response('index.html', locals())

def login_view(request):
	if request.GET.has_key('next'):
		next = request.GET['next']
	else:
		next = '/main'

	if request.user.is_authenticated():
		return HttpResponseRedirect('/main')
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
def main(request):
	return render_to_response('main.html', locals())

