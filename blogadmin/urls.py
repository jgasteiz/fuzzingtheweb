from django.conf.urls import patterns, url
from django.views.generic import RedirectView

urlpatterns = patterns(

    'blogadmin.views',

    url(r'^$', RedirectView.as_view(url='post/'), name='home_admin'),

    # Post
    url(r'^post/(?P<pk>[\d]+)/edit/$', 'edit_post', name='edit_post'),
    url(r'^post/(?P<pk>[\d]+)/delete/$', 'delete_post', name='delete_post'),
    url(r'^post/add/$', 'create_post', name='create_post'),
    url(r'^post/$', 'list_post', name='list_post'),
)
