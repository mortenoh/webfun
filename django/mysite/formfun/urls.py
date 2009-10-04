from django.conf.urls.defaults import *
import views

urlpatterns = patterns('',
	(r'^1/$', views.form1),
	(r'^2/$', views.form2),
	(r'^search/$', views.search),
)

