from __future__ import unicode_literals
from ..login.models import User
from django.db import models

class AuthorManager(models.Manager):
    def add_author(self, request):
        errors = []
        try:
            author = Author.objects.get(name=request.POST['new_author_name'])
        except:
            errors.append("Author already exists. Please use drop down.")
            return (False, errors)
        author = Author.objects.create(name=request.POST['new_author_name'])
        return (True, errors)
class BookManager(models.Manager):
    def add_book(self, request):
        new_book = Book.objects.create(title=request.POST['title'], author=author)
        return new_book

class ReviewManager(models.Manager):
    def add_review(self, request, new_book_id):
        book = Book.objects.get(id=new_book_id)
        user = User.objects.get(id=request.session['user']['user_id'])
        review = Review.objects.create(content=request.POST['review'], creator=user, reviewed_book=book, rating=request.POST['rating'])

    def destroy(self, request, id):
        Review.objects.get(id=id).delete()


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
