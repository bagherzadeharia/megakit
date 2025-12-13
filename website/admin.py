from django.contrib import admin
from website.models import Contact

class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = (
        'name',
        'email',
        'subject',
        'created_date',
    )
    list_filter = ('email',)
    search_fields = ('name', 'message')
    fields = (
        'message',
        'name',
        'email',
        'subject',
    )

admin.site.register(Contact, ContactAdmin)