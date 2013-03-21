from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    'news.views',
    url(r'^$', 'hacker_news', name='hacker_news'),
)
