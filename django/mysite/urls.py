from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

import formfun.urls

urlpatterns = patterns('',
	(r'^form/', include(formfun.urls)),
    (r'^admin/', include(admin.site.urls)),
)

