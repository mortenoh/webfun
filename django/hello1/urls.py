from django.conf.urls.defaults import *

from hello1.simple.models import Person

from django.contrib import admin
admin.autodiscover()

class PersonAdmin(admin.ModelAdmin):
	date_hierarchy = 'birthdate'
	list_display = ('name', 'birthcountry', 'gender')

admin.site.register(Person, PersonAdmin)

urlpatterns = patterns('',
    (r'^simple/', include('hello1.simple.urls')),
    (r'^admin/', include(admin.site.urls)),
)
