from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import HomeView
from django.contrib import admin


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('admin/', admin.site.urls),

    # for users
    path('accounts/', include('allauth.urls')),
    # path('games/', include('games.urls')),
    path('articles/', include('articles.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns