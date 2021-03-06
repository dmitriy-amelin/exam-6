from django.shortcuts import render, get_object_or_404, redirect
from guest_book.forms import ReviewForm
from guest_book.models import GuestBook, status_choices


def index_view(request):
    guest_book = GuestBook.objects.filter(status="active").order_by('-created_at')

    return render(request, 'index.html', {'guest_book': guest_book})


def add_review(request):
    if request.method == 'GET':
        form = ReviewForm()
        return render(request, 'add_review.html', context={'form': form, 'choices': status_choices})