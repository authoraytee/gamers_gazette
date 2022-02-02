from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Article, UserArticleRelation

from accounts.models import CustomUser

class ArticleReaderSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name')

class ArticlesSerializer(ModelSerializer): 
    rating = serializers.DecimalField(max_digits=3, decimal_places=2)
    likes = serializers.IntegerField(read_only=True)

    owner_name = serializers.CharField(source='owner.username', default="", read_only=True)
    readers = ArticleReaderSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = ('id', 'title', 'link', 'text', 'site', 'pub_date', 'rating', 'likes', 'owner_name', 'readers')


class UserArticleRelationSerializer(ModelSerializer):
    class Meta:
        model = UserArticleRelation
        fields = ('article', 'like', 'in_bookmarks', 'rate')