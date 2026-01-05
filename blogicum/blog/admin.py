from django.contrib import admin
from .models import Category, Location, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Управление категориями."""

    list_display = ('title', 'slug', 'is_published', 'created_at')
    list_editable = ('is_published',)
    search_fields = ('title', 'slug')
    list_filter = ('is_published', 'created_at')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    """Управление географическими метками."""

    list_display = ('name', 'is_published', 'created_at')
    list_editable = ('is_published',)
    search_fields = ('name',)
    list_filter = ('is_published', 'created_at')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Управление публикациями."""

    list_display = (
        'title', 'category', 'location', 'author', 'pub_date', 'is_published')
    list_editable = ('is_published',)
    search_fields = ('title', 'text', 'author__username')
    list_filter = (
        'category', 'location', 'author', 'is_published', 'pub_date',
        'created_at')
    date_hierarchy = 'pub_date'
    raw_id_fields = ('author',)
