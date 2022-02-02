from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import UpdateModelMixin
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from core.permissions import IsOwnerOrReadOnly
from django.shortcuts import render
from django.db.models import Avg

from django.db.models import Case, Count, When

from .serializers import GamesSerializer, UserGameRelationSerializer
from .models import Game, UserGameRelation


class GameViewSet(ModelViewSet):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Game.objects.all().annotate(
        likes=Count(Case(When(usergamerelation__like=True, then=1))),
        rating=Avg('usergamerelation__rate')
        ).prefetch_related('subscribers')
    serializer_class = GamesSerializer
    #filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # filter_fields = ['name', 'platforms', 'genres', 'tags']   
    # search_fields = ['name']
    # ordering_fields = ['name', 'platforms', 'genres', 'tags', 'metacritic_rating', 'esb_rating']


class UserGameRelationView(UpdateModelMixin, GenericViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = UserGameRelation.objects.all()
        
    serializer_class = UserGameRelationSerializer
    lookup_field = 'game'

    def get_object(self):
        obj, created = UserGameRelation.objects.get_or_create(
            user=self.request.user,
            game_id=self.kwargs['game']) 

        return obj
