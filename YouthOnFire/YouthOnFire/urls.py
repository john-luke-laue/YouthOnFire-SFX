from django.conf.urls import patterns, include, url

from django.conf import settings


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from dajaxice.core import dajaxice_autodiscover, dajaxice_config
dajaxice_autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'YouthOnFire.views.home', name='home'),
    # url(r'^YouthOnFire/', include('YouthOnFire.foo.urls')),
    url(r'^$', include('main.urls', namespace="main")),
    url(r'^home/', 'main.views.index'),
    url(r'^events/', 'main.views.events'),
    url(r'^calendar/', 'main.views.calendar'),

    (r'^%s/' % settings.DAJAXICE_MEDIA_PREFIX, include('dajaxice.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),


    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)




urlpatterns += staticfiles_urlpatterns()

