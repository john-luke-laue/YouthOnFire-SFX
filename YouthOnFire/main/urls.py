from django.conf.urls import patterns, url, include

from main import views
from django.conf import settings

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from dajaxice.core import dajaxice_autodiscover, dajaxice_config
dajaxice_autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'main.views.index', name='index'),
	(r'^%s/' % settings.DAJAXICE_MEDIA_PREFIX, include('dajaxice.urls')),

)


urlpatterns += staticfiles_urlpatterns()