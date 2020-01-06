from django.contrib import admin

from content.models import Category, Content, Comment, File

admin.site.register(Content)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(File)
