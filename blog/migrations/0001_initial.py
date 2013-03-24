# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'NavItem'
        db.create_table(u'blog_navitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('url', self.gf('django.db.models.fields.CharField')(default='', max_length=240, null=True, blank=True)),
            ('weight', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'blog', ['NavItem'])

        # Adding model 'Widget'
        db.create_table(u'blog_widget', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40, blank=True)),
            ('body', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('weight', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'blog', ['Widget'])

        # Adding model 'Tag'
        db.create_table(u'blog_tag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=60)),
        ))
        db.send_create_signal(u'blog', ['Tag'])

        # Adding model 'File'
        db.create_table(u'blog_file', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('upload_path', self.gf('django.db.models.fields.files.FileField')(default='', max_length=100)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=240, blank=True)),
        ))
        db.send_create_signal(u'blog', ['File'])

        # Adding model 'Post'
        db.create_table(u'blog_post', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=120, blank=True)),
            ('body', self.gf('django.db.models.fields.TextField')()),
            ('published', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 3, 24, 0, 0))),
            ('live', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('page', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'blog', ['Post'])

        # Adding M2M table for field mytags on 'Post'
        db.create_table(u'blog_post_mytags', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('post', models.ForeignKey(orm[u'blog.post'], null=False)),
            ('tag', models.ForeignKey(orm[u'blog.tag'], null=False))
        ))
        db.create_unique(u'blog_post_mytags', ['post_id', 'tag_id'])


    def backwards(self, orm):
        # Deleting model 'NavItem'
        db.delete_table(u'blog_navitem')

        # Deleting model 'Widget'
        db.delete_table(u'blog_widget')

        # Deleting model 'Tag'
        db.delete_table(u'blog_tag')

        # Deleting model 'File'
        db.delete_table(u'blog_file')

        # Deleting model 'Post'
        db.delete_table(u'blog_post')

        # Removing M2M table for field mytags on 'Post'
        db.delete_table('blog_post_mytags')


    models = {
        u'blog.file': {
            'Meta': {'object_name': 'File'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'upload_path': ('django.db.models.fields.files.FileField', [], {'default': "''", 'max_length': '100'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '240', 'blank': 'True'})
        },
        u'blog.navitem': {
            'Meta': {'ordering': "('weight',)", 'object_name': 'NavItem'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'url': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '240', 'null': 'True', 'blank': 'True'}),
            'weight': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'blog.post': {
            'Meta': {'ordering': "('-published',)", 'object_name': 'Post'},
            'body': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'live': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'mytags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['blog.Tag']", 'null': 'True', 'blank': 'True'}),
            'page': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'published': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 3, 24, 0, 0)'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '120', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '120'})
        },
        u'blog.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        u'blog.widget': {
            'Meta': {'ordering': "('weight',)", 'object_name': 'Widget'},
            'body': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'weight': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['blog']