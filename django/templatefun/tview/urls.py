
from django.conf.urls.defaults import *

urlpatterns = patterns('tview.views',
	(r'^add/', 'add'),
	(r'^$', 'model1'),
	(r'^id/(?P<cid>\d)', 'view_id'),
)

