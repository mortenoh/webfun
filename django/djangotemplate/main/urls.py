
from django.conf.urls.defaults import *

urlpatterns = patterns('djangotemplate.main',
	(r'^$', 'views.index'),
)

