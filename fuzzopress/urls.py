from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

from fuzzopress.blog.views import BlogView, BlogPostView, AboutView

urlpatterns = patterns('',
	url(r'^$',
		BlogView.as_view(),
		name='blog'),
	url(r'^single/(?P<slug>[-\w]+)$',
		BlogPostView.as_view(),
		name='post'),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^about-fuzzopress/',
		AboutView.as_view(
			template_name = "about/aboutfuzzopress.html"),
		name='aboutfuzzopress'),
	url(r'^about-me/',
		AboutView.as_view(
			template_name = "about/aboutme.html"),
		name='aboutme'),
)
