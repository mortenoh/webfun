
from django.conf.urls.defaults import *

urlpatterns = patterns('main',
	(r'^$', 'views.index'),
	(r'^(?P<n>\d+)$','views.index2'),
)

