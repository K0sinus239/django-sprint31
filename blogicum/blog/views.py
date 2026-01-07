from django.utils import timezone

from django.shortcuts import render, get_object_or_404

from .models import Post, Category

from .constants import POSTS_IN_PAGE


def get_published_posts():
    """Возвращает QuerySet опубликованных постов."""
    return Post.objects.filter(
        is_published=True,
        pub_date__lte=timezone.now(),
        category__is_published=True
    ).select_related('category', 'author', 'location')


def index(request):
    posts = get_published_posts()[:POSTS_IN_PAGE]
    context = {'post_list': posts}
    return render(request, 'blog/index.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(
        Post,
        id=post_id,
        is_published=True,
        pub_date__lte=timezone.now(),
        category__is_published=True
    )
    context = {'post': post}
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    posts = get_published_posts().filter(category=category)
    context = {
        'post_list': posts,
        'category_slug': category_slug,
    }
    return render(request, 'blog/category.html', context)
