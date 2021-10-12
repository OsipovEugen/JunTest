from rest_framework import serializers, permissions, viewsets, generics
from post.models import Post
from authentication.models import User

class PostSerializer(serializers.ModelSerializer):
	class Meta:
		model = Post
		fields = ('title', 'body', 'created', 'slug', 'author', 'total_likes')