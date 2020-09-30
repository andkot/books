from django.contrib import admin
from django.urls import path

from .views import (
    BookListAPIView,
    BookDetailsAPIView,
    UpdateBookAPIView,
    DestroyBookAPIView,
    CreateBookAPIView,
)

urlpatterns = [
    path('', BookListAPIView.as_view(), name='book-list'),
    path('<int:pk>', BookDetailsAPIView.as_view(), name='book-details'),
    path('<int:pk>/update', UpdateBookAPIView.as_view(), name='book-update'),
    path('<int:pk>/destroy', DestroyBookAPIView.as_view(), name='book-destroy'),
    path('create', CreateBookAPIView.as_view(), name='book-create')
]
