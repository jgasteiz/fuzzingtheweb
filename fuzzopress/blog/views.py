# -*- coding: utf-8 -*-
from django.views.generic.dates import YearArchiveView, MonthArchiveView, DayArchiveView
from django.views.generic import ListView, DetailView, TemplateView
from django.shortcuts import get_object_or_404
from fuzzopress.blog.models import Post, NavItem, Widget

class CustomContextMixin(object):
    """
    Same context data for every class view
    """
    def get_context_data(self, **kwargs):
        context = super(CustomContextMixin, self).get_context_data(**kwargs)
        context.update({ 'navItems': NavItem.objects.all(), 'widgets': Widget.objects.all() })
        return context

class BlogPostView(CustomContextMixin, DetailView):
    """
    A single post view
    """
    context_object_name='post'

    def get_object(self):
        return get_object_or_404(Post, slug=self.kwargs['slug'])    

class BlogView(CustomContextMixin, ListView):
    """
    Main blog view
    """
    paginate_by = 3
    context_object_name = 'post_list'

    def get_queryset(self):
        return Post.objects.published()

class AboutView(CustomContextMixin, TemplateView):
    """
    For static pages. template_name can be set here or in urls.py
    """

class CustomDateMixin(CustomContextMixin, object):
    """
    Same date_field and context_object_name for every Dated-class view
    """
    date_field = 'published'
    context_object_name = 'post_list'

    def get_queryset(self):
        return Post.objects.published()

class ArchiveDay(CustomDateMixin, DayArchiveView):
    """
    For a day
    """
    month_format='%m'

class ArchiveMonth(CustomDateMixin, MonthArchiveView):
    """
    For a month
    """
    month_format='%m'

class ArchiveYear(CustomDateMixin, YearArchiveView):
    """
    For a year
    """
    make_object_list=True
