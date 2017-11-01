from django.conf.urls import url

from . import views

app_name = 'main'
urlpatterns = [
	url(r'^$', views.homepage, name='homepage'),
	url(r'^facilities/$', views.facilities, name='facilities'),
	url(r'^projects/$', views.projects, name='projects'),
	url(r'^publications/$', views.publications, name='publications'),
	url(r'^contact/$', views.contact, name='contact'),
	url(r'^atoms/$', views.atoms, name='atoms'),
	#url(r'^admin/$', views.django_admin_page, name='django_admin_page'), #link to admin
	url(r'^flatten/$', views.flatten, name='flatten'),


	url(r'^projects/actinide_water_abs/$', views.actinide_water_abs, name='actinide_water_abs'),
	]
