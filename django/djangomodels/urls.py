
from django.conf.urls.defaults import *

from djangomodels.main.models import *

from django.contrib import admin
admin.autodiscover()
admin.site.register(Person)
admin.site.register(Student)
admin.site.register(University)
admin.site.register(Course)

urlpatterns = patterns('',
	(r'^main', include('djangomodels.main.urls')),
    (r'^admin/', include(admin.site.urls)),
)

