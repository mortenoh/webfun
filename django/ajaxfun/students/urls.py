
from django.conf.urls.defaults import *

urlpatterns = patterns('ajaxfun.students.views',
	(r'^/$', 'index'),
	(r'^/check/$', 'check_username'),
	(r'^/count/plaintext/$', 'count_plaintext'),
	(r'^/count/json/$', 'count_json'),
	(r'^/count/xml/$', 'count_xml'),
)

