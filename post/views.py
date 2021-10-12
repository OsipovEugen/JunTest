from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status, generics
from django.http import Http404
from rest_framework.response import Response
from rest_framework import serializers, permissions, viewsets
from .models import Post
from .serializers import PostSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated

class PostDetailView(APIView):
	permission_classes = [IsAuthenticated]
	def get(self, request, slug):
		author = Post.objects.get(slug=slug)
		serializer = PostSerializer(author)
		return Response(serializer.data)

	def put(self, request, slug): # Изменение поста
		post = Post.objects.get(slug=slug)
		serializer = PostSerializer(post, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


	def delete(self, request, slug): # Удаление заметок
		post = Post.objects.get(slug=slug)
		post.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

class PostView(APIView):
	permission_classes = [AllowAny]
	""" Вывод всех постов и создание поста """# permission_classes = [AllowAny]
	def get(self, request): # Вывод всех заметок пользователя
	# posts = Post.objects.filter(author=request.user.id) # Вывод всех заметок пользователя
		posts = Post.objects.all() # Вывод BCEX заметок 
		serializer = PostSerializer(posts, many=True)
		return Response(serializer.data)

	def post(self, request): # Создание заметок
		post = PostSerializer(data=request.data)
		if post.is_valid(raise_exception=True):
			post.save()
		return Response(status=status.HTTP_201_CREATED)
