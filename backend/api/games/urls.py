from rest_framework.routers import SimpleRouter
from .viewsets import GameViewSet, UserGameRelationView

router = SimpleRouter()
router.register(r'', GameViewSet)
router.register(r'game_relation', UserGameRelationView)

urlpatterns = []

urlpatterns += router.urls
