from django.contrib import admin
from authentication.models import *
from post.models import Post
from like.models import Like


class UserAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name', 'email', 'is_staff')
# Register your models here.


class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'body')


class LikeAdmin(admin.ModelAdmin):
	list_display = ('user', 'date')

admin.site.register(User, UserAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Like, LikeAdmin)

