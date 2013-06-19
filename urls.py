from django.contrib import admin
from django.conf.urls import patterns, include, url
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^loginadmin/', include(admin.site.urls)),
    url(r'^admin/', include('blogadmin.urls')),
    url(r'', include('blog.urls')),
)
