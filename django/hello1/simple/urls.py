
from django.conf.urls.defaults import *

urlpatterns = patterns('simple.views',
#   (r'1/$', 'index1'),
#    (r'2/$', 'index2'),
	(r'(?P<n>\d+)/$', 'index'),
	(r't/$', 't'),
)
