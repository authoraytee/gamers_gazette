from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Game, UserGameRelation

from accounts.models import CustomUser

class GameSubscriberSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name')

class GamesSerializer(ModelSerializer): 
    rating = serializers.DecimalField(max_digits=3, decimal_places=2)
    likes = serializers.IntegerField(read_only=True)

    subscribers = GameSubscriberSerializer(many=True, read_only=True)

    class Meta:
        model = Game
        fields = ('id', 'name', 'release_date', 'platforms', 'requirements', 'genres', 'tags', 'metacritic_rating', 'esb_rating', 'rating', 'likes', 'subscribers')

class UserGameRelationSerializer(ModelSerializer):
    class Meta:
        model = UserGameRelation
        fields = ('game', 'like', 'in_bookmarks', 'rate')