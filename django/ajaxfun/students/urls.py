
from django.conf.urls.defaults import *

urlpatterns = patterns('ajaxfun.students.views',
	(r'^/$', 'index'),
	(r'^/count/$', 'count'),
)

