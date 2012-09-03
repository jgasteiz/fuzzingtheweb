# -*- coding: utf-8 -*-
from django.contrib import admin
from markitup.widgets import AdminMarkItUpWidget
from fuzzopress.blog.models import Post, NavItem, Widget, Tag, File


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'published', 'draft')
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'body':
            kwargs['widget'] = AdminMarkItUpWidget()
        return super(PostAdmin, self).formfield_for_dbfield(db_field, **kwargs)


class NavItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url', 'weight')


class WidgetAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'weight')


class FileAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'upload_path', 'url')
    readonly_fields = ('url',)


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(NavItem, NavItemAdmin)
admin.site.register(Widget, WidgetAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(File, FileAdmin)
admin.site.register(Tag, TagAdmin)
