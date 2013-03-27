from django.conf.urls import patterns, url
from .views import SimplePage

urlpatterns = patterns(
    'blog.views',

    url(r'^$', 'home_page', name='home_page'),
    url(r'^hacker_news/',
        SimplePage.as_view(template_name='hacker_news.html'),
        name='hacker_news'),

    url(r'^404/', 'four_o_four', name='404'),
    url(r'^500/', 'five_hundred', name='500'),

    # Ajax requests
    url(r'^_ajax/archive/(?P<year>\d+)/(?P<month>\d+)/$', 'load_entries', name='load_entries'),
    url(r'^_ajax/night-mode/(?P<layout>[-\w]+)', 'night_mode', name='night_mode'),

    # List entries by tag
    url(r'^tag/(?P<tag>[-\w]+)/', 'tag_page', name='tag_page'),

    # Search stuff
    url(r'^search/(?P<search>[-\w]+)', 'search_page', name='search_page'),

    # Archive
    url(r'^archive/', 'archive_page', name='archive_page'),

    # A post or page
    url(r'^(?P<slug>[-\w]+)/', 'entry_page', name='entry_page'),
)
