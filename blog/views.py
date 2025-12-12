from django.utils import timezone
from django.http import Http404
from django.contrib import messages
from django.shortcuts import get_object_or_404, render
from blog.models import *
from blog.forms import *

def blog_home(request, **kwargs):
    try:
        posts = Post.objects.filter(
            published_date__lte=timezone.now(),
            status=1
        )
    except Http404 or ValueError:
        return render(request, "error-404.html")
    else:
        if kwargs.get('categoryName') is not None:
            posts = posts.filter(
                category__name=kwargs['categoryName']
            ).order_by('-published_date')
            context = {
                'posts': posts,
            }
            return render(request, 'blog/blog-home.html', context)

        # if kwargs.get('tagName') is not None:
        #     posts = posts.filter(
        #         tags__name=kwargs['tagName']
        #     ).order_by('-published_date')
        #     context = {
        #         'posts': posts,
        #     }
        #     return render(request, 'blog/blog-home.html', context)

        if kwargs.get('authorUsername') is not None:
            posts = posts.filter(
                author__username=kwargs['authorUsername']
            ).order_by('-published_date')
            context = {
                'posts': posts,
            }
            return render(request, 'blog/blog-home.html', context)

        # try:
        #     posts = Paginator(posts, per_page=4)
        #     pageNumber = request.GET.get('page')
        #     posts = posts.page(pageNumber)
        # except PageNotAnInteger:
        #     posts = posts.page(1)
        # except EmptyPage:
        #     return render(request, "error-404.html")

        context = {
            'posts': posts,
        }
        return render(request, 'blog/blog-home.html', context)

def blog_single(request, postID):
    try:
        post = get_object_or_404(
            Post,
            id=postID,
            published_date__lte=timezone.now(),
            status=1
        )
    except Http404 or ValueError:
        return render(request, 'error-404.html')
    else:
        previous_post = Post.objects.filter(
            published_date__lt=post.published_date,
            published_date__lte=timezone.now(),
            status=1
        ).order_by('-published_date').first()
        next_post = Post.objects.filter(
            published_date__gt=post.published_date,
            published_date__lte=timezone.now(),
            status=1,
        ).order_by('published_date').first()

        if request.method == 'POST':
            commentForm = CommentForm(request.POST)
            if commentForm.is_valid():
                temp = commentForm.save(commit=False)
                temp.post = post
                temp.save()
                messages.success(request, 'Your ticket has been submitted successfully')
            else:
                messages.error(request, 'Your ticket has not been submitted')
                print(commentForm.errors)
        else:
            commentForm = CommentForm()

        if not post.login_required:
            post.counted_views += 1
            post.save()
            comments = Comment.objects.filter(
                post = post.id,
                approved = 1
            )
            context = {
                'previousPost': previous_post,
                'post': post,
                'nextPost': next_post,
                'comments': comments,
                'commentForm': commentForm
            }
            return render(request, 'blog/blog-single.html', context)
        else:
            if request.user.is_authenticated:
                post.counted_views += 1
                post.save()
                comments = Comment.objects.filter(
                    post = post.id,
                    approved = 1
                )
                context = {
                    'previousPost': previous_post,
                    'post': post,
                    'nextPost': next_post,
                    'comments': comments,
                    'commentForm': commentForm
                }
                return render(request, 'blog/blog-single.html', context)
            else:
                return blog_home(request)

def blog_search(request):
    pass