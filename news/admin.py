# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import NewsFeed


class NewsFeedAdmin(admin.ModelAdmin):
    list_display = ('id', 'json', 'created')


admin.site.register(NewsFeed, NewsFeedAdmin)
