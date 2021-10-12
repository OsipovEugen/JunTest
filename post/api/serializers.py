from rest_framework import serializers, permissions, viewsets, generics
from post.models import Post
from authentication.models import User
from django.contrib.auth import get_user_model

from rest_framework import serializers
from like import services as likes_services
from ..models import Post

class PostSerializer(serializers.ModelSerializer):
    is_fan = serializers.SerializerMethodField()

    
    class Meta:
        model = Post
        fields = ('title', 'body', 'created', 'slug', 'author', 'total_likes', 'is_fan', 'id')

    def get_is_fan(self, obj) -> bool:
        """Проверяет, лайкнул ли `request.user` твит (`obj`)"""
        user = self.context.get('request').user
        return likes_services.is_fan(obj, user)


