# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime
from django.utils.timezone import utc
from blog.utils import uuslug as slugify
from django.utils.translation import ugettext_lazy as __


class PostManager(models.Manager):
    def published(self):
        return self.filter(
            live=True,
            page=False,
            published__lte=datetime.utcnow().replace(tzinfo=utc))


class NavItem(models.Model):
    """ Primary nav bar items """
    name = models.CharField(__('Name'), blank=False, max_length=40)
    url = models.CharField(__('Url'), blank=True, null=True, default='', max_length=240)
    weight = models.IntegerField(default=0)

    class Meta:
        ordering = ('weight',)

    def __unicode__(self):
        return self.name


class Widget(models.Model):
    """ Sidebar items """
    name = models.CharField(__('Name'), blank=True, max_length=40)
    body = models.TextField(__('Body'), blank=True)
    weight = models.IntegerField(default=0)

    class Meta:
        ordering = ('weight',)

    def __unicode__(self):
        return self.name


class Tag(models.Model):
    """ Tag item """
    name = models.CharField(__('Name'), max_length=60)

    def __unicode__(self):
        return self.name


class File(models.Model):
    """ File item """
    title = models.CharField(__('Title'), blank=False, max_length=120)
    upload_path = models.FileField(
        __('File'),
        blank=False,
        upload_to='%Y/%m/%d',
        default='',
        help_text='Select a file to upload')
    url = models.CharField(__('Url'), blank=True, max_length=240)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.url = self.upload_path.url
        super(File, self).save(*args, **kwargs)


class Post(models.Model):
    """ Blog entry items """
    title = models.CharField(__('Title'), blank=False, max_length=120)
    slug = models.SlugField(__('Slug'), blank=True, max_length=120)
    body = models.TextField(__('Body'))
    published = models.DateTimeField(
        __('Publish Date'),
        default=datetime.now,
        help_text=__('Future-dated posts will only be published at the \
            specified date and time.'))
    live = models.BooleanField(
        default=False,
        help_text=__('If checked, won\'t be displayed in the public site.'))
    page = models.BooleanField(
        default=False,
        help_text=__('If checked, this will be a page, not a blog post. It \
            will be useful for "about" pages and so.'))

    objects = PostManager()
    mytags = models.ManyToManyField("Tag", blank=True, null=True)

    class Meta:
        ordering = ('-published',)
        get_latest_by = ('published',)
        verbose_name, verbose_name_plural = 'Blog Post', 'Blog Posts'

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title, instance=self)
        super(Post, self).save(*args, **kwargs)
