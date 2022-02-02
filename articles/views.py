from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import UpdateModelMixin
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from core.permissions import IsOwnerOrReadOnly
from django.shortcuts import render
from django.db.models import Avg

from django.db.models import Case, Count, When

from .serializers import ArticlesSerializer, UserArticleRelationSerializer
from .models import Article, UserArticleRelation


class ArticleViewSet(ModelViewSet):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Article.objects.all().annotate(
        likes=Count(Case(When(userarticlerelation__like=True, then=1))),
        rating=Avg('userarticlerelation__rate')
        ).select_related('owner').prefetch_related('readers')
    serializer_class = ArticlesSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['pub_date']   
    search_fields = ['title']
    ordering_fields = ['price']

    # Переопределение perform_create из ModelViewSet класса
    def perform_create(self, serializer):
        serializer.validated_data['owner'] = self.request.user
        serializer.save()


class UserArticleRelationView(UpdateModelMixin, GenericViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = UserArticleRelation.objects.all()
        
    serializer_class = UserArticleRelationSerializer
    lookup_field = 'article'

    def get_object(self):
        obj, created = UserArticleRelation.objects.get_or_create(
            user=self.request.user,
            article_id=self.kwargs['article']) 

        return obj
