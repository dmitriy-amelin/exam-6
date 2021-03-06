from django.contrib import admin
from guest_book.models import GuestBook


class GuestBookAdmin(admin.ModelAdmin):
    readonly_fields = ('author', 'email', 'text')
    list_display = ['author', 'email', 'text', 'created_at', 'updated_at', 'status']
    list_filter = ['status', 'created_at']
    search_fields = ['status', 'created_at']
    fields = ['author', 'email', 'text', 'status', 'updated_at']


admin.site.register(GuestBook, GuestBookAdmin)