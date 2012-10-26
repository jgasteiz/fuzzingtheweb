from django.contrib import admin
from django.conf.urls import patterns, include, url
from fuzzopress.blog.views import (BlogView, PostView, ArchiveMonth, TagView, SearchView)
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$',
        BlogView.as_view(),
        name='blog'),

    url(r'^admin/', include(admin.site.urls)),

    # List entries by tag
    url(r'^tag/(?P<tag>[-\w]+)/',
        TagView.as_view(),
        name='tag'),

    # Search stuff
    url(r'^search/(?P<search>[-\w]+)',
        SearchView.as_view(),
        name='search'),

    # Archive
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/',
        ArchiveMonth.as_view(),
        name='archive_month'),

    # A post or page
    url(r'^(?P<slug>[-\w]+)/',
        PostView.as_view(),
        name='post'),

)
