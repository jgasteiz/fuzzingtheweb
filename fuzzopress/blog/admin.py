# -*- coding: utf-8 -*-
from django.contrib import admin
from markitup.widgets import AdminMarkItUpWidget
from fuzzopress.blog.models import Post, NavItem, Widget

class PostAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'slug', 'body', 'created', 'updated_at', 'published', 'draft')
	def formfield_for_dbfield(self, db_field, **kwargs):
		if db_field.name == 'body':
			kwargs['widget'] = AdminMarkItUpWidget()
		return super(PostAdmin, self).formfield_for_dbfield(db_field, **kwargs)

class NavItemAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'url', 'weight')

class WidgetAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'body', 'weight')

admin.site.register(Post, PostAdmin)
admin.site.register(NavItem, NavItemAdmin)
admin.site.register(Widget, WidgetAdmin)