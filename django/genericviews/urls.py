from django.conf.urls.defaults import *
from django.contrib import admin

from gview.models import Student

admin.autodiscover()
admin.site.register(Student)

urlpatterns = patterns('',
    (r'^', include('gview.urls')),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
)

