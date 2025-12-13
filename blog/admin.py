from django.contrib import admin
from blog.models import Post, Category, Comment
from django_summernote.admin import SummernoteModelAdmin

class CategoryAdmin(admin.ModelAdmin):
    fields = (
        'name',
    )
    exclude = ()
    list_display = (
        'name',
    )

class CommentAdmin(SummernoteModelAdmin):
    summernote_fields = ('message',)
    fields = (
        'name',
        'email',
        'message',
        'post',
        'approved'
    )
    exclude = ()
    list_display = (
        'name',
        'email',
        'created_date',
        'post',
        'approved'
    )
    date_hierarchy = 'created_date'
    ordering = ('created_date',)
    list_filter = ('post', 'approved')
    empty_value_display = '-empty-'

class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    date_hierarchy = 'created_date'
    empty_value_display = '--empty--'
    fields = (
        'title',
        'content',
        'author',
        'image',
        'category',
        'counted_views',
        'status',
        'published_date',
        'tags',
        'login_required'
    )
    exclude = ()
    list_display = (
        'title',
        'counted_views',
        'author',
        # 'tags',
        'status',
        'created_date',
        'published_date'
    )
    ordering = ('published_date',)
    list_filter = ('status',)
    search_fields = ('title', 'content')

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Category, CategoryAdmin)