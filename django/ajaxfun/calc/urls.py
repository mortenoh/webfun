
from django.conf.urls.defaults import *

urlpatterns = patterns('ajaxfun.calc.views',
	(r'^/$', 'index'),
	(r'^/eval/$', 'eval_view'),
)

