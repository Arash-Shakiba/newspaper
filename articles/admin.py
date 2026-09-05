from django.contrib import admin
from django.template.defaultfilters import title

from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "body",
        "author",
        "date",
    ]

admin.site.register(Article, ArticleAdmin)
