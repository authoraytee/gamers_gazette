
from rest_framework.permissions import BasePermission, SAFE_METHODS

# Переопределение класса IsAuthenticatedOrReadOnly из rest_framework 
# нашел соурс код на гитхабе папка rest_framework файл permissions.py

class IsOwnerOrReadOnly(BasePermission):

    # Поменял с has_permission на has_object_permission + добавил в аргументы obj
    # has_object_permission работает для тех url, где должен передаваться id
    # то есть update, delete, create
    def has_object_permission(self, request, view, obj):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_authenticated and obj.owner == request.user
            # В строке выше добавил obj.owner == request.user
            # Именно эта часть строки говорит о том, что создавать, изменять и удалять
            # может только автор книги, а остальные могут читать
        )