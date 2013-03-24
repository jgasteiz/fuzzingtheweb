from django.conf.urls import patterns, url

urlpatterns = patterns(
    'news.views',
    url(r'^get_news/', 'get_news', name='get_news'),
    url(r'^update_feed/', 'update_feed', name='update_feed'),
)
