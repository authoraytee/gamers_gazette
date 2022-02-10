from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import HomeView


urlpatterns = [
    path('admin/', include('admin_custom.urls')),

    path('', HomeView.as_view(), name='home'),

    # for users
    path('accounts/', include('allauth.urls')),
    path('api/', include('api.urls')),

    path('test/', include('just_tests.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# url example for debug_toolbar
# http://localhost:8000/api/articles/?debug-toolbar
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns