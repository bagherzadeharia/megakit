from django import template
from blog.models import Post
from django.utils import timezone

register = template.Library()

@register.inclusion_tag("website/blog-latest-posts.html")
def blog_latest_posts():
    posts = Post.objects.filter(
        status=1,
        published_date__lte=timezone.now(),
    ).order_by('-published_date')[:3]
    return {'posts': posts}