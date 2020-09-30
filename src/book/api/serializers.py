from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from ..models import Book

class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author_name']

class BookDetailsSerializer(BookSerializer):
    title = serializers.CharField(required=False)
    author_name = serializers.CharField(required=False)
    description = serializers.CharField(required=False)
    class Meta:
        model = Book
        fields = '__all__'