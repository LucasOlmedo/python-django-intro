from django.db import models
from uuid import uuid4

# Create your models here.

def upload_book_cover(instance, filename):
    return f"{instance.id}-{filename}"

class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    release_year = models.IntegerField()
    state = models.CharField(max_length=50)
    pages = models.IntegerField()
    publishing_company = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    book_cover = models.ImageField(upload_to=upload_book_cover, blank=True, null=True)
