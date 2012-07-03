from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

from fuzzopress.blog.views import BlogView, BlogPostView, AboutView, ArchiveMonth, ArchiveYear

urlpatterns = patterns('',
    url(r'^$',
        BlogView.as_view(),
        name='blog'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^about-fuzzopress/',
        AboutView.as_view(
            template_name = "about/aboutfuzzopress.html"),
        name='about_fuzzopress'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/$',
        ArchiveMonth.as_view(),
        name='archive_month'),
    url(r'^(?P<year>\d{4})/$',
        ArchiveYear.as_view(),
        name='archive_year'),
    url(r'^(?P<slug>[-\w]+)$',
        BlogPostView.as_view(),
        name='post'),
)
