from rest_framework.routers import SimpleRouter
from .viewsets import ArticleViewSet, UserArticleRelationView

router = SimpleRouter()
router.register(r'', ArticleViewSet)
router.register(r'article_relation', UserArticleRelationView)

urlpatterns = []

urlpatterns += router.urls
