from dataclasses import field
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Article, UserArticleRelation, Comment

from accounts.models import CustomUser

class ReaderSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name')

class CommentSerializer(ModelSerializer):
    # Fist and seconds name calls is one sql request (so it's ok)
    author_first_name = serializers.CharField(source='author.first_name', default="", read_only=True)
    author_last_name = serializers.CharField(source='author.last_name', default="", read_only=True)

    class Meta:
        model = Comment
        fields = ('comment', 'author_first_name', 'author_last_name')

class ArticlesSerializer(ModelSerializer): 
    rating = serializers.DecimalField(max_digits=3, decimal_places=2)
    likes = serializers.IntegerField(read_only=True)

    owner_name = serializers.CharField(source='owner.username', default="", read_only=True)
    readers = ReaderSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = ('id', 'title', 'link', 'text', 'site', 'pub_date', 'cover', 'rating', 'likes', 'owner_name', 'readers', 'comments')


class UserArticleRelationSerializer(ModelSerializer):
    class Meta:
        model = UserArticleRelation
        fields = ('article', 'like', 'in_bookmarks', 'rate')