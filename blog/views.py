from blog.forms import *
from blog.models import *
from django.db.models import Q
from django.http import Http404
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import *
from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def blog_home(request, **kwargs):
    try:
        posts = Post.objects.filter(
            published_date__lte=timezone.now(),
            status=1
        )
    except Http404 or ValueError:
        return render(request, "404.html", status=404)
    else:
        if kwargs.get('categoryName') is not None:
            posts = posts.filter(
                category__slug=kwargs['categoryName']
            ).order_by('-published_date')
            context = {
                'categoryName': Category.objects.get(slug=kwargs['categoryName']).name,
                'posts': posts,
            }
            return render(request, 'blog/blog-home.html', context)

        if kwargs.get('tagName') is not None:
            posts = posts.filter(
                tags__name=kwargs['tagName']
            ).order_by('-published_date')
            context = {
                'tagName': kwargs['tagName'],
                'posts': posts,
            }
            return render(request, 'blog/blog-home.html', context)

        if kwargs.get('authorUsername') is not None:
            posts = posts.filter(
                author__username=kwargs['authorUsername']
            ).order_by('-published_date')
            print(User.objects.get(username=kwargs['authorUsername']).first_name, User.objects.get(username=kwargs['authorUsername']).last_name)
            context = {
                'authorFirstName': User.objects.get(username=kwargs['authorUsername']).first_name,
                'authorLastName': User.objects.get(username=kwargs['authorUsername']).last_name,
                'posts': posts,
            }
            return render(request, 'blog/blog-home.html', context)

        try:
            posts = Paginator(posts, per_page=4)
            pageNumber = request.GET.get('page')
            posts = posts.page(pageNumber)
        except PageNotAnInteger:
            posts = posts.page(1)
        except EmptyPage:
            return render(request, "404.html")

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
        return render(request, '404.html', status=404)
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
                return render(request, '403.html', status=403)

def blog_search(request):
    if (request.method == 'GET') and (query := request.GET.get('s')): # Used a Warlus Operator, Declaring a Variable (query) in "If" Statement and Using it in This Specific Scope
        posts = Post.objects.filter(
            status=1,
            published_date__lte=timezone.now()
        ).filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
        )
        context = {
            'query': query,
            'posts': posts
        }
        return render(request, "blog/blog-home.html", context)
    else:
        return blog_home(request)

@login_required
def blog_new_post(request):
    if request.method == 'POST':
        form = CreatePostForm(request.POST, request.FILES)
        if form.is_valid():
            temp = form.save(commit=False)
            temp.author = request.user
            temp.save()
            messages.success(request, 'The new post has been created successfully.')
            return redirect('blog:blog_home')
        else:
            messages.error(request, 'The new post has not been created.')
    else:
        form = CreatePostForm()

    context = {
        'form': form
    }
    return render(request, 'blog/blog-create-post.html', context)
