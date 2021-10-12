from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from authentication.models import User
from django.utils.text import slugify
from time import time
from like.models import Like


def gen_slug(s):
	new_slug = slugify(s, allow_unicode=True)
	return new_slug + '-' + str(int(time()))


class Post(models.Model):
	title = models.CharField(max_length=50, blank=False, verbose_name='Название поста')
	body = models.TextField(max_length=500, blank=True, verbose_name='Текст поста')
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now_add=True, verbose_name='Время написания поста')
	updated = models.DateTimeField(auto_now=True)
	slug = models.SlugField(unique=True, blank=True, allow_unicode=True)
	likes = GenericRelation(Like)

	class Meta:
		verbose_name = 'Пост'
		verbose_name_plural = 'Посты'
		ordering = ['created']

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = gen_slug(self.title)
		super().save(*args, **kwargs)

	@property
	def total_likes(self):
		return self.likes.count()