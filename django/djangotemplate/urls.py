
from django.conf import settings
from django.conf.urls.defaults import *

urlpatterns = patterns('',
	(r'^', include('djangotemplate.main.urls')),

	(r'^r/(?P<path>.*)$', 'django.views.static.serve',
		{'document_root' : settings.STATIC_MEDIA_PREFIX}),
)

