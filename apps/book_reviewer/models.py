from __future__ import unicode_literals
from ..login.models import User
from django.db import models

class BookManager(models.Manager):
    def add_book(self, request):
        errors = []

        if request.POST['author_name'] == "" and request.POST['new_author_name'] == "":
            errors.append('Please select or enter an author.')
            return (False, errors)
        elif request.POST['author_name'] == "":
            author = Author.objects.create(name=request.POST['new_author_name'])
        else:
            author = Author.objects.get(id=request.POST['author_name'])

        new_book = Book.objects.create(title=request.POST['title'], author=author)
        return (True, new_book)

class ReviewManager(models.Manager):
    def add_review(self, request, new_book_id):
        book = Book.objects.get(id=new_book_id)
        reviewer = User.objects.get(id=request.session['user']['user_id'])
        review = Review.objects.create(content=request.POST['review'], creator=reviewer, reviewed_book=book, rating=request.POST['rating'])

    def destroy(self, request, id):
        Review.objects.get(id=id).delete()


class Author(models.Model):
    name = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

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
