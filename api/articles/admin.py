from atexit import register
from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Article, UserArticleRelation, Comment

class CommentInline(admin.StackedInline):
    model = Comment

@admin.register(Article)
class ArticleAdmin(ModelAdmin):
    list_display = ('title', 'site', 'pub_date')
    inlines = [CommentInline, ]

@admin.register(UserArticleRelation)
class UserArticleRelationAdmin(ModelAdmin):
    pass

@admin.register(Comment)
class CommentAdmin(ModelAdmin):
    list_display = ('article', 'author', 'comment')



