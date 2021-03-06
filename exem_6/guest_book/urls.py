from django.urls import path

from guest_book.views import (
    index_view,
    add_review,
    review_view,
    review_update_view,
    review_delete_view,

)

urlpatterns = [
    path('', index_view, name='review-list'),
    path('review/add/', add_review, name='add_review'),
    path('review/<int:pk>', review_view, name='review-view'),
    path('<int:pk>/update', review_update_view, name='review-update'),
    path('<int:pk>/delete', review_delete_view, name='review-delete'),

]