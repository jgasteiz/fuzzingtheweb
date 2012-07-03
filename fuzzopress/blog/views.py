# -*- coding: utf-8 -*-
from django.views.generic.dates import YearArchiveView, MonthArchiveView, DayArchiveView
from django.views.generic import ListView, DetailView, TemplateView
from fuzzopress.blog.models import Post, NavItem, Widget
from django.shortcuts import get_object_or_404
from datetime import date

class CustomContextMixin(object):
    """
    Same context data for every class view
    """
    def get_context_data(self, **kwargs):
        context = super(CustomContextMixin, self).get_context_data(**kwargs)
        arch = Post.objects.dates('published', 'month', order='DESC')
        archives = {}
        for i in arch:
            year = i.year
            month = i.month
            try:
                archives[year][month-1][1] = True
            except KeyError:
                # catch the KeyError, and set up list for that year
                archives[year] = [[date(year, m ,1),False] for m in xrange(1,13)]
                archives[year][month-1][1] = True
        context.update({
            'archives': sorted(archives.items(),reverse=True),
            'navItems': NavItem.objects.all(), 
            'widgets': Widget.objects.all() })
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
    model = Post
    context_object_name = 'post_list'

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
