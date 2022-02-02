from rest_framework.routers import SimpleRouter
from .views import ArticleViewSet, UserArticleRelationView

router = SimpleRouter()
router.register(r'', ArticleViewSet)
router.register(r'article_relation', UserArticleRelationView)

urlpatterns = []

urlpatterns += router.urls
