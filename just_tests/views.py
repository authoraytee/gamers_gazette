from django.views.generic import ListView
from api.games.models import Game
from api.articles.models import Article

class GamesTestList(ListView):
    model = Game
    template_name = "test/games_test.html"

class ArticlesTestList(ListView):
    model = Article
    template_name = "test/articles_test.html"