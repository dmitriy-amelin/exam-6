from django.shortcuts import render, get_object_or_404, redirect
from guest_book.models import GuestBook


def index_view(request):
    guest_book = GuestBook.objects.all()

    return render(request, 'index.html', {'guest_book': guest_book})

