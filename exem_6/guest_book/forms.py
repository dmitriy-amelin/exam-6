from django import forms

from guest_book.models import GuestBook


class ReviewForm(forms.ModelForm):

    class Meta:
        model = GuestBook
        fields = ('author', 'email', 'text')


