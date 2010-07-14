
from django.conf.urls.defaults import *

urlpatterns = patterns('',
	(r'^',		include('djangourls.main.urls')),
)

