"""JunTest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from authentication.views import EugenView, StatView, LastLogin
from django.urls import re_path


from post.models import *
from post.serializers import *
from post.views import *


from rest_framework_simplejwt import views as djoser_views
from rest_framework.routers import DefaultRouter
from djoser import views


router = DefaultRouter()
router.register("register", views.UserViewSet)





urlpatterns = [
    path('api/', include('post.api.urls', namespace='api')),# Лайк, Анлайк, фаны


    path('admin/', admin.site.urls),


    path('api/post/<str:slug>/', PostDetailView.as_view()), # Информация про определенный пост
    path('api/posts/', PostView.as_view()),# Просмотр постов


    path('last_login/',LastLogin.as_view() ), # 
    path('stat/',StatView.as_view() ),# Статистика лайков
    path('eugen/',EugenView.as_view() ), # Для теста того, что jwt токен передается в запросе и успешно проходит проверку
    path('', include(router.urls)), # Регистрация пользователя
    path("login/", djoser_views.TokenObtainPairView.as_view(), name="jwt-create"), 
 ]




# http://localhost:8000/api/posts/1/fans/
# http://localhost:8000/api/posts/1/unlike/
# http://localhost:8000/api/posts/1/like/
# http://127.0.0.1:8000/stat/?date_from=2021-10-05&date_to=2021-10-12
#