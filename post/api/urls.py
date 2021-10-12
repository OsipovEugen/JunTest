# tweets/api/urls.py

from rest_framework.routers import DefaultRouter

from .viewsets import PostViewSet
# Создаем router и регистрируем ViewSet
router = DefaultRouter()
router.register('posts', PostViewSet)

# URLs настраиваются автоматически роутером
urlpatterns = router.urls
app_name = 'post'
