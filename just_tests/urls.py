from urllib.parse import urlparse
from django.urls import path
from .views import GamesTestList, ArticlesTestList

urlpatterns = [
    path('games/', GamesTestList.as_view(), name='games_test'),
    path('articles/', ArticlesTestList.as_view(), name='articles_test'),
]