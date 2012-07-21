# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime
from django.utils.timezone import utc
from fuzzopress.blog.utils import uuslug as slugify
from django.utils.translation import ugettext_lazy as __


class PostManager(models.Manager):
    def published(self):
        return self.filter(draft=False, published__lte=datetime.utcnow().replace(tzinfo=utc))


class NavItem(models.Model):
    """
    Primary nav bar items
    """
    name = models.CharField(__('Name'), blank=False, max_length=40)
    url = models.CharField(__('Url'), blank=False, max_length=240)
    weight = models.IntegerField(default=0)

    class Meta:
        ordering = ('weight',)

    def __unicode__(self):
        return self.name


class Widget(models.Model):
    """
    Sidebar items
    """
    name = models.CharField(__('Name'), blank=True, max_length=40)
    body = models.TextField(__('Body'), blank=True)
    weight = models.IntegerField(default=0)

    class Meta:
        ordering = ('weight',)

    def __unicode__(self):
        return self.name


class Tag(models.Model):
    """
    Tag item
    """
    name = models.CharField(__('Name'), max_length=60)

    def __unicode__(self):
        return self.name


class Post(models.Model):
    """
    Blog entry items
    """
    title = models.CharField(__('Title'), blank=False, max_length=120)
    slug = models.SlugField(__('Slug'), blank=True, max_length=120)
    body = models.TextField(__('Body'))
    created = models.DateTimeField(__('Creation Date'), auto_now_add=True)
    updated_at = models.DateTimeField(__('Last Updated'), auto_now=True)
    published = models.DateTimeField(__('Publish Date'), default=datetime.utcnow().replace(tzinfo=utc), help_text=__('Future-dated posts will only be published at the specified date and time.'))
    draft = models.BooleanField(default=False, help_text=__('If checked, will not be displayed in the public site.'))

    objects = PostManager()
    mytags = models.ManyToManyField("Tag", blank=True, null=True)

    class Meta:
        ordering = ('-published',)
        get_latest_by = ('published',)
        verbose_name, verbose_name_plural = 'Blog Post', 'Blog Posts'

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('post', None,
                    {'slug': self.slug
                })

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title, instance=self)
        super(Post, self).save(*args, **kwargs)
