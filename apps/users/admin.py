from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

from apps.blog.models import Post

User = get_user_model()

admin.site.register(User, UserAdmin)

admin.site.register(Post)