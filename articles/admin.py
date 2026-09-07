from django.contrib import admin
from django.template.defaultfilters import title

from .models import Article, Comment

class CommentAdmin(admin.ModelAdmin):
    list_display = [
        "author",
        "comment",
        "article",
        "date",
    ]

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0

class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]
    list_display = [
        "title",
        "body",
        "author",
        "date",
    ]

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
