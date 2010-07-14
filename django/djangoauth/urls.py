from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	(r'^main/$', 'djangoauth.main.views.main'),
	(r'^accounts/login/$', 'djangoauth.main.views.login_view'),
	(r'^accounts/logout/$', 'djangoauth.main.views.logout_view'),
	(r'^$', 'djangoauth.main.views.index'),

    (r'^admin/', include(admin.site.urls)),
)

