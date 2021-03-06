from django.contrib import admin
from guest_book.models import GuestBook


class GuestBookAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'email', 'text', 'status', 'created_at', 'updated_at', 'status']
    list_filter = ['status', 'created_at']
    search_fields = ['status', 'created_at']
    fields = ['id', 'author', 'email', 'text', 'created_at', 'updated_at', 'status']


admin.site.register(GuestBook, GuestBookAdmin)