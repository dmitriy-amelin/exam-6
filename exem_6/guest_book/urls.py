from django.urls import path

from guest_book.views import (
    index_view,
    add_review,

)

urlpatterns = [
    path('', index_view, name='review-list'),
    path('review/add/', add_review, name='add_review'),

]