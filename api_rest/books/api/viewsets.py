from books import models
from books.api import serializers
from rest_framework import viewsets

class BookViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.BookSerializer
    queryset = models.Book.objects.all()