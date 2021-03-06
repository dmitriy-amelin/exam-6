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
    elif request.method == 'POST':
        form = ReviewForm(data=request.POST)
        if form.is_valid():
            review = GuestBook.objects.create(
                author=form.cleaned_data.get("author"),
                email=form.cleaned_data.get("email"),
                text=form.cleaned_data.get("text")
            )
            return redirect('review-list')
        return render(request, 'add_review.html', context={'form': form, 'choices': status_choices})


def review_view(request, pk):
    review = get_object_or_404(GuestBook, id=pk)
    return render(request, 'review-view.html', context={'review': review})


def review_update_view(request, pk):
    review = get_object_or_404(GuestBook, id=pk)

    if request.method == 'GET':
        form = ReviewForm(initial={
            'author': review.author,
            'email': review.email,
            'text': review.text
        })
        return render(request, 'review-update.html', context={'form': form, 'review': review})
    elif request.method == 'POST':
        form = ReviewForm(data=request.POST)
        if form.is_valid():
            review.author = request.POST.get("author")
            review.email = request.POST.get("email")
            review.text = request.POST.get("text")
            review.save()
            return redirect('review-list')

        return render(request, 'review-update.html', context={'form': form, 'review': review})


def review_delete_view(request, pk):
    review = get_object_or_404(GuestBook, id=pk)

    if request.method == 'GET':
        return render(request, 'review-delete.html', context={'review': review})
    elif request.method == 'POST':
        review.delete()
        return redirect('review-list')