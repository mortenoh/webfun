from django.conf.urls.defaults import *
from django.contrib import admin
from django.views.generic.simple import direct_to_template
from django.views.generic import list_detail

from models import Student

student_info = {
	'queryset' : Student.objects.all(),
	'template_name' : 'students.html',
	'template_object_name' : 'student',
}

urlpatterns = patterns('gview.views',
    (r'^$', 'index'),
	(r'^about/$', direct_to_template, {
		'template' : 'about.html',
	}),
	(r'^students/$', list_detail.object_list, student_info),
)
