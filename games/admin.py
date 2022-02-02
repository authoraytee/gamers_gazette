from atexit import register
from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Game, UserGameRelation

@admin.register(Game)
class GameAdmin(ModelAdmin):
    # list_display = ('title', 'site', 'pub_date')
    pass

@admin.register(UserGameRelation)
class UserGameRelationAdmin(ModelAdmin):
    pass