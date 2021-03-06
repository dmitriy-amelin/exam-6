from django.urls import path

from guest_book.views import (
    index_view,

)

urlpatterns = [
    path('', index_view, name='review-list'),

]