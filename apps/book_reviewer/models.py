from __future__ import unicode_literals
from ..login.models import User
from django.db import models

class AuthorManager(models.Manager):
    def add_author(self, request):
        pass

class BookManager(models.Manager):
    def add_book(self, request):
        pass

class ReviewManager(models.Manager):
    def add_review(self, request):
        pass
    def destroy_review(self, request):
        pass


class Author(models.Model):
    name = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = AuthorManager()

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, related_name='books')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()

class Review(models.Model):
    content = models.CharField(max_length=255)
    creator = models.ForeignKey(User, related_name='reviews')
    reviewed_book = models.ForeignKey(Book, related_name='books_reviews')
    rating = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ReviewManager()
