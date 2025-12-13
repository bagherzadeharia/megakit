from django.db import models
from django.db.models.fields import EmailField
from django.views.decorators.http import require_POST

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_date']
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'