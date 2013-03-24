# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'NewsFeed'
        db.create_table(u'news_newsfeed', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('json', self.gf('django.db.models.fields.TextField')()),
            ('created', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'news', ['NewsFeed'])


    def backwards(self, orm):
        # Deleting model 'NewsFeed'
        db.delete_table(u'news_newsfeed')


    models = {
        u'news.newsfeed': {
            'Meta': {'ordering': "('-created',)", 'object_name': 'NewsFeed'},
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'json': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['news']