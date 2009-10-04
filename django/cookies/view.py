
from django.http import HttpResponse, HttpRequest

def index(request):
	if "color" in request.COOKIES:
		return HttpResponse("color: %s" % request.COOKIES["color"]);
	else:
		return HttpResponse("No color defined.")

def set(request):
	if "color" in request.GET:
		response = HttpResponse("color: %s" % request.GET["color"])
		response.set_cookie("color", request.GET["color"])
		return response
	else:
		return HttpResponse("No color given.")

