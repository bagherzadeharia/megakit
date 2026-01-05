from django import forms
from blog.models import Comment, Post
from django_summernote.admin import SummernoteWidget
# from captcha.fields import CaptchaField

class CommentForm(forms.ModelForm):
    # captcha = CaptchaField()
    class Meta:
        model = Comment
        fields = ('name', 'email', 'message')

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'image', 'tags', 'category', 'login_required')
