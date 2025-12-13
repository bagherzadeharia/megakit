from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms

class PasswordResetRequestForm(forms.Form):
    email = forms.EmailField(max_length=255)

class PasswordResetNewPasswordForm(forms.Form):
    password = forms.CharField(max_length=255)
    confirmPassword = forms.CharField(max_length=255)