# -*- coding: utf-8 -*-
from django.views.generic.dates import YearArchiveView, MonthArchiveView, DayArchiveView
from django.views.generic import ListView, DetailView, TemplateView
from django.shortcuts import get_object_or_404
from fuzzopress.blog.models import Post, NavItem, Widget

class BlogPostView(DetailView):
    context_object_name='post'
    # allow_empty = True

    def get_object(self):
        return get_object_or_404(Post, slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super(BlogPostView, self).get_context_data(**kwargs)
        context.update({ 'navItems': NavItem.objects.all(), 'widgets': Widget.objects.all() })
        return context

class BlogView(ListView):
    paginate_by=2
    context_object_name='post_list'

    def get_queryset(self):
        return Post.objects.published()

    def get_context_data(self, **kwargs):
        context = super(BlogView, self).get_context_data(**kwargs)
        context.update({ 'navItems': NavItem.objects.all(), 'widgets': Widget.objects.all() })
        return context

class AboutView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context.update({ 'navItems': NavItem.objects.all(), 'widgets': Widget.objects.all() })
        return context

class CustomDateMixin(object):
    date_field='published'
    context_object_name='post_list'

    def get_queryset(self):
        return Post.objects.published()


class ArchiveDay(CustomDateMixin, DayArchiveView):
    month_format='%m'


class ArchiveMonth(CustomDateMixin, MonthArchiveView):
    month_format='%m'


class ArchiveYear(CustomDateMixin, YearArchiveView):
    make_object_list=True
