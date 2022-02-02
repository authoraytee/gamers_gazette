from django.urls import path, include

urlpatterns = [
    path('games/', include('games.urls')),
    path('articles/', include('articles.urls')),
]