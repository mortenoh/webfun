
from django.http import HttpResponse
from models import Student

def index(request):
	return HttpResponse("Hello.")

