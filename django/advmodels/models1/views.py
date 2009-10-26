
from django.http import HttpResponse
from django.core import serializers

from models import Student

def index(request):
	response = HttpResponse(mimetype="text/javascript")
	serializers.serialize("json", Student.objects.all(), stream=response,
			fields=('first_name', 'last_name'))
	return response

