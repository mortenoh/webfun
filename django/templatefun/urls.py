from django.conf.urls.defaults import *
from django.contrib import admin
from tview.models import Student, Course

admin.autodiscover()
admin.site.register(Student)
admin.site.register(Course)

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
	(r'^', include('tview.urls')),
)

