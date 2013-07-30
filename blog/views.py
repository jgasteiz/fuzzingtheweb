# -*- coding: utf-8 -*-
import calendar
import json
from datetime import date

from django.conf import settings
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, View, TemplateView

from rest_framework.renderers import JSONRenderer

from blogapi.serializers import PostSerializer

from .models import Post, NavItem, Widget, Tag
from .utils import get_query as get_search_query


# Base views
class CustomContextMixin(object):
    """ Same context data for every class view """
    paginate_by = settings.FUZZOPRESS_SETTINGS['entries_per_page']
    context_object_name = 'posts'
    template_name = 'post_list.html'

    def get_context_data(self, **kwargs):
        context = super(CustomContextMixin, self).get_context_data(**kwargs)
        context.update({
            'navItems': NavItem.objects.all(),
            'widgets': Widget.objects.all(),
            'tags': Tag.objects.all(),
            'settings': settings.FUZZOPRESS_SETTINGS,
            'request': self.request})
        return context


# API views
class PostListJSON(View):
    def get(self, request, *args, **kwargs):
        post_qs = Post.objects.filter(live=True, page=False)

        # Paginate the results
        paginator = Paginator(post_qs, 10)
        page_num = 1
        if 'page' in request.GET:
            page_num = int(request.GET.get('page', 1))
        page = paginator.page(page_num)

        post_serializer = PostSerializer(page.object_list)
        post_list = JSONRenderer().render(post_serializer.data)
        return HttpResponse(post_list, mimetype='application/json')

post_list_json = PostListJSON.as_view()


# Page views
class PostList(CustomContextMixin, ListView):
    """ Main blog view """
    def get_queryset(self):
        return Post.objects.published()

post_list = PostList.as_view()


class TagPage(CustomContextMixin, ListView):
    """ A tag posts """
    def get_queryset(self):
        return Post.objects.published().filter(mytags__name=self.kwargs['tag'])

tag_page = TagPage.as_view()


class SearchPage(CustomContextMixin, ListView):
    """ A search result posts """
    def get_queryset(self):
        query_string = self.kwargs['search']
        if query_string:
            entry_query = get_search_query(query_string, ['title', 'body'])
            return Post.objects.published().filter(entry_query)
        return Post.objects.published()

search_page = SearchPage.as_view()


class PostDetail(CustomContextMixin, DetailView):
    """ A single post view """
    context_object_name = 'post'
    template_name = 'post_detail.html'

    def get_object(self):
        return get_object_or_404(Post, slug=self.kwargs['slug'])

post_detail = PostDetail.as_view()


class ArchivePage(CustomContextMixin, ListView):
    """ For a month """
    context_object_name = 'archives'
    template_name = 'post_archive.html'

    def get_queryset(self):
        archive = {}
        archive_qs = Post.objects.dates(
            'published',
            'month',
            order='ASC').reverse()
        for arch in archive_qs:
            year = arch.year
            month = arch.month
            try:
                archive[year][month - 1][1] = True
            except KeyError:
                archive[year] = [[date(year, m, 1), False] for m in xrange(1,
                                                                           13)]
                archive[year][month - 1][1] = True
        for year in archive:
            archive[year] = reversed(archive[year])
        return [sorted(archive.items(), reverse=True)]

archive_page = ArchivePage.as_view()


# Ajax views
class NightMode(CustomContextMixin, View):
    def get(self, request, *args, **kwargs):
        request.session['layout'] = self.kwargs['layout']
        return HttpResponse(request.session['layout'])

night_mode = NightMode.as_view()


class LoadEntries(View):
    def get(self, request, *args, **kwargs):
        year = ''
        month = ''
        if self.kwargs['year'] and self.kwargs['month']:
            year = self.kwargs['year']
            month = self.kwargs['month']
            posts_qs = Post.objects.published().filter(published__year=year,
                                                       published__month=month)
            posts = []
            for post in posts_qs:
                posts.append({
                    'title': '<span class="date">%s %s.</span> %s' % (
                        post.published.day,
                        calendar.month_abbr[post.published.month],
                        post.title),
                    'url': '/%s/' % (post.slug)
                })
            return HttpResponse(json.dumps(posts))
        return HttpResponse('Nothing found')

load_entries = LoadEntries.as_view()


class Error(CustomContextMixin, TemplateView):
    pass

four_o_four = Error.as_view(template_name='404.html')
five_hundred = Error.as_view(template_name='500.html')
