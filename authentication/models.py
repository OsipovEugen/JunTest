from django.db import models
import jwt
import re
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

from datetime import datetime, timedelta
from .validators import validate_first_name, validate_last_name, validate_email_domain
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin




class UserManager(BaseUserManager):
# Django требует, чтобы кастомные пользователи определяли свой собственный
# класс Manager. Унаследовавшись от BaseUserManager, мы получаем много того
# же самого кода, который Django использовал для создания User.

	def create_user(self, email, password, first_name, last_name)	:
		""" Создает и возвращает пользователя с имэйлом, паролем, first_name, last_name. """
		if email is None:
			raise TypeError('Users must have an email address.')
		user = self.model(
			first_name=first_name, 
			email=email,
			password=password,
			last_name=last_name,
			)
		user.set_password(password)
		# user.password = make_password(password)
		user.save()

		return user

	def create_superuser(self, email, password, first_name, last_name):
		user = self.create_user(
		email=email,
		password=password,
		first_name=first_name,
		last_name=last_name
		)
		user.is_superuser = True
		user.is_staff = True
		user.save()

		return user





class User(AbstractBaseUser, PermissionsMixin):
	
	first_name = models.CharField(validators=[validate_first_name],max_length=30, blank=False)
	last_name = models.CharField(validators=[validate_last_name],max_length=30, blank=False)
	email = models.EmailField(
		validators=[validate_email_domain, validate_email],
		db_index=True,
		unique=True,
		)
	password = models.CharField(unique=True, db_index=True, max_length=16)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now_add=True)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['first_name', 'last_name']


# Сообщает Django, что определенный выше класс UserManager
# должен управлять объектами этого типа.
	objects = UserManager()

	def __str__(self):
		return self.email

	@property
	def get_full_name(self):
		return self.first_name + ' ' + self.last_name






