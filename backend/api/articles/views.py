from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import UpdateModelMixin

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from api.permissions import IsOwnerOrReadOnly
from django.db.models import Avg

from django.db.models import Case, Count, When

from .serializers import ArticlesSerializer
from .models import Article, UserArticleRelation


class ArticleViewSet(ModelViewSet):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Article.objects.all().annotate(
        likes=Count(Case(When(userarticlerelation__like=True, then=1))),
        rating=Avg('userarticlerelation__rate')
        ).select_related('owner').prefetch_related('readers')
    serializer_class = ArticlesSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['title', 'site', 'link'] # ?title=title 
    search_fields = ['title', 'site'] # ?search=title (вместо title сам название)
    ordering_fields = ['pub_date', 'rating', 'likes'] # ?ordering=rating

    # Переопределение perform_create из ModelViewSet класса
    def perform_create(self, serializer):
        serializer.validated_data['owner'] = self.request.user
        serializer.save()


class UserArticleRelationView(UpdateModelMixin, GenericViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = UserArticleRelation.objects.all()
