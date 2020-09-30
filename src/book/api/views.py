from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    CreateAPIView,
)
from .serializers import (
    BookSerializer,
    BookDetailsSerializer,
)

from ..models import Book


class BookListAPIView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetailsAPIView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDetailsSerializer


class UpdateBookAPIView(UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDetailsSerializer


class DestroyBookAPIView(DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class CreateBookAPIView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDetailsSerializer
