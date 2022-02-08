from django.contrib import admin 
from django.urls import path
from .views import AdminHomeView

urlpatterns = [
    path('django/', admin.site.urls),

    path('', AdminHomeView.as_view(), name='admin_home'),
]