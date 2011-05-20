from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
import os.path

# Enable autoadmin
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
   # media files
   url(r'^(?P<path>favicon\.ico)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
   url(r'^(?P<path>robots\.txt)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
   url(r'^(?P<path>[^/]*\.png)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
   url(r'^css/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.join(settings.MEDIA_ROOT, 'css')}),
   url(r'^js/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.join(settings.MEDIA_ROOT, 'js')}),

   # admin stuff
   url(r'^static/admin/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.ADMIN_MEDIA_ROOT}),
   url(r'^admin/', include(admin.site.urls)),

   # other
   url(r'^$', 'views.home', name='home'),
)
