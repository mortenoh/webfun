
from django.conf.urls.defaults import *

urlpatterns = patterns('',
	(r'^secret/$', 'theview.views.secret'),
	(r'^accounts/logout/$', 'theview.views.logout_view'),
	(r'^accounts/login/$', 'theview.views.login_view'),
	(r'^$', 'theview.views.index'),
)

