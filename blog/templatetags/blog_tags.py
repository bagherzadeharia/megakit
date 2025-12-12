from django import template
from blog.models import Comment, Post, Category
from django.utils import timezone

register = template.Library()

@register.simple_tag(name="commentCounter")
def commentCounter(postID):
    post = Post.objects.get(pk=postID)
    commentCount = Comment.objects.filter(
        approved=1,
        post=post.id
    ).count()
    return commentCount

@register.filter
def truncate_chars(text, charNumber):
    return text[:charNumber ] + '...'

@register.inclusion_tag('blog/blog-latest-posts.html')
def latest_posts():
    posts = Post.objects.filter(
        status=1,
        published_date__lte=timezone.now(),
    ).order_by('published_date')[:3]
    return {'posts': posts}

@register.inclusion_tag('blog/blog-post-category.html')
def category():
    posts = Post.objects.filter(
        status=1,
        published_date__lte=timezone.now(),
    )
    cat_dict = {}
    categories = Category.objects.all()
    for cat in categories:
        cat_dict[cat] = posts.filter(category=cat).count()

    return {
        'categories': cat_dict
    }