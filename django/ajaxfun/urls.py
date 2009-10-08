
from django.conf.urls.defaults import *
from django.contrib import admin
from ajaxfun.students.models import Student
from django.conf import settings

admin.autodiscover()
admin.site.register(Student)

urlpatterns = patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT }),
	(r'^students', include('ajaxfun.students.urls')),
	(r'^calc', include('ajaxfun.calc.urls')),

	(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	(r'^admin/', include(admin.site.urls)),
)

