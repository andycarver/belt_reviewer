from django.shortcuts import render, redirect
from django.contrib import messages
from models import Book, Review, Author, User

def index(request):
    if session_check(request):
        context = {
            'recent_reviews': Review.objects.order_by('-created_at')[:3],
            'all_books': Book.objects.all()
        }
        return render(request, "book_reviewer/index.html", context)

    return redirect('login:index')

def show_editor(request):
    if session_check(request):
        context = {
            'authors': Author.objects.all()
        }

        return render(request, 'book_reviewer/add.html', context)

    return redirect('login:index')

def add_book_and_review(request):
    if session_check(request):
        result = Book.objects.add_book(request)
        if result[0]==False:
            print_errors(request, result[1])
            return redirect('book:editor')

        Review.objects.add_review(request, result[1].id)

        return redirect('book:show_book', result[1].id)

    return redirect('login:index')

def print_errors(request, error_list):
    for error in error_list:
        messages.add_message(request, messages.INFO, error)

def add_review(request, id):
    Review.objects.add_review(request, id)

    return redirect('book:show_book', id)

def show_book(request, id):
    if session_check(request):
        context = {
            'book': Book.objects.get(id=id),
            'reviews': Review.objects.filter(reviewed_book=id)
        }

        return render(request, 'book_reviewer/show_book.html', context)

    return redirect('login:index')

def show_user(request, id):
    if session_check(request):
        context = {
            'user': User.objects.get(id=id),
            'reviewed_books': Book.objects.filter(books_reviews__creator__id=id)
        }
        return render(request, 'book_reviewer/show_user.html', context)

    return redirect('login:index')

def destroy(request, review_id, book_id):
    if session_check(request):
        Review.objects.destroy(request, review_id)

        return redirect('book:show_book', book_id)

    return redirect('login:index')

def logout(request):
    request.session.clear()

    return redirect('login:index')

def session_check(request):
    if 'user' in request.session:
        return True
    else:
        return False
