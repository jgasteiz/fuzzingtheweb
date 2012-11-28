from django.contrib import admin
from django.conf.urls import patterns, include, url
from fuzzopress.blog.views import (BlogView, PostView, ArchiveView, TagView,
    SearchView, LoadEntries)
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$',
        BlogView.as_view(),
        name='blog'),

    url(r'^admin/', include(admin.site.urls)),

    # Ajax requests
    url(r'^_ajax/archive/(?P<year>\d+)/(?P<month>\d+)/$',
        LoadEntries.as_view(),
        name='load_entries'),

    # List entries by tag
    url(r'^tag/(?P<tag>[-\w]+)/',
        TagView.as_view(),
        name='tag'),

    # Search stuff
    url(r'^search/(?P<search>[-\w]+)',
        SearchView.as_view(),
        name='search'),

    # Archive
    url(r'^archive/',
        ArchiveView.as_view(),
        name='archive'),

    # A post or page
    url(r'^(?P<slug>[-\w]+)/',
        PostView.as_view(),
        name='post')
)
