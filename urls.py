from django.conf.urls.defaults import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings


# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
# Examples:
# url(r'^$', 'fromthepit.views.home', name='home'),
# url(r'^fromthepit/', include('fromthepit.foo.urls')),

# Uncomment the admin/doc line below to enable admin documentation:
# url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

# Uncomment the next line to enable the admin:
#url(r'^admin/', include(admin.site.urls)),
url(r'^$', 'fromthepit.views.hello'),
url(r'^pictures/$', 'fromthepit.views.showPictures'),
url(r'^coachella/$', 'fromthepit.views.showPicturesCoachella'),
)

if settings.DEBUG:
	urlpatterns += staticfiles_urlpatterns()