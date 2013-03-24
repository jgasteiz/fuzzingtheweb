from django.db import models
from datetime import datetime


class FeedManager(models.Manager):
    def latest(self):
        return self.all()[0]


class NewsFeed(models.Model):
    json = models.TextField()
    created = models.DateTimeField()

    objects = FeedManager()

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return self.created

    def save(self, *args, **kwargs):
        if not self.created:
            self.created = datetime.now()
        super(NewsFeed, self).save(*args, **kwargs)
