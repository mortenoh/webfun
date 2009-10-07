
from django.conf.urls.defaults import *

urlpatterns = patterns('ajaxfun.students.views',
	(r'^/$', 'index'),
	(r'^/count/plaintext/$', 'count_plaintext'),
	(r'^/count/json/$', 'count_json'),
	(r'^/count/xml/$', 'count_xml'),
)

