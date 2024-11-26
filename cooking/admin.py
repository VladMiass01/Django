from django.contrib import admin
from .models import Category, Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')
    list_display_links = ('title', 'category')


admin.site.register(Category)
admin.site.register(Post, PostAdmin)
