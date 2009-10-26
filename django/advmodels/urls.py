
from django.conf.urls.defaults import *
from django.contrib import admin
from models1.models import Student, Course


class StudentAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name', 'enrolled', 'last_updated')
	date_hierarchy = 'enrolled'
	ordering = ['-enrolled']
	search_fields = ['first_name', 'last_name']

class CourseAdmin(admin.ModelAdmin):
	list_display = ('name', 'display_name', 'last_updated')
	search_fields = ['name', 'display_name']


admin.autodiscover()
admin.site.register(Student, StudentAdmin)
admin.site.register(Course, CourseAdmin)

urlpatterns = patterns('',
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^', include('advmodels.models1.urls')),
)

