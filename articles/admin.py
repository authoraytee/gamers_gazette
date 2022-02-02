from atexit import register
from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Article, UserArticleRelation

@admin.register(Article)
class ArticleAdmin(ModelAdmin):
    pass

@admin.register(UserArticleRelation)
class UserArticleRelationAdmin(ModelAdmin):
    pass