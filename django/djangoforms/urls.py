from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	(r'^$', 'djangoforms.main.views.index'),
    (r'^admin/', include(admin.site.urls)),
)
