from rest_framework.routers import SimpleRouter
from .views import GameViewSet, UserGameRelationView

router = SimpleRouter()
router.register(r'', GameViewSet)
router.register(r'game_relation', UserGameRelationView)

urlpatterns = []

urlpatterns += router.urls
