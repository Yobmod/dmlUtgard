from django.conf.urls import url

from . import views

app_name = 'main'
urlpatterns = [
	url(r'^$', views.homepage, name='homepage'),
	url(r'^facilities/$', views.facilities, name='facilities'),
	url(r'^projects/$', views.facilities, name='projects'),
	url(r'^publications/$', views.publications, name='publications'),
	url(r'^contact/$', views.contact, name='contact'),
	#url(r'^admin/$', views.django_admin_page, name='django_admin_page'), #link to admin

	]
