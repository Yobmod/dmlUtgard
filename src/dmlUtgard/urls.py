from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage

admin.autodiscover()

urlpatterns = [

    url(r'^admin/', admin.site.urls),
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	url(r'^api/auth/', include('rest_framework.urls', namespace='rest_framework')),
	url(r'^favicon.ico$', RedirectView.as_view(url=staticfiles_storage.url('icons/favicon.ico'), permanent=False), name="favicon"),

    url(r'^', include("main.urls", namespace='main')),
	#url(r'^api/', include("main.api.urls", namespace='main-api')),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
