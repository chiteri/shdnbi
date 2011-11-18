from django.conf.urls.defaults import patterns, include, url
from shdnbi.views import home 
import os 

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'shdnbi.views.home', name='home'),
    # url(r'^shdnbi/', include('shdnbi.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^static_media/(?P<path>.*)$', 'django.views.static.serve', 
    { 'document_root': os.path.join(os.path.dirname(__file__), 'static').replace('\\','/') }), 
    (r'^$', home),
    (r'^post/', include('shdnbi.post.urls')), 
    (r'^comments/', include('django.contrib.comments.urls')), 
    (r'', include('django.contrib.flatpages.urls')), 
)
