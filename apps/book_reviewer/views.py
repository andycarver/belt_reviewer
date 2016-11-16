from django.shortcuts import render, redirect

from models import Book, Review, Author

def index(request):
    return render(request, "book_reviewer/index.html")

def show_editor(request):
    context = {
        'authors': Author.objects.all()
    }
    return render(request, 'book_reviewer/add.html', context)

def add_book_and_review(request):
    new_book = Book.objects.add_book(request)
    Review.objects.add_review(request, new_book.id)
    author_result=Author.objects.add_author(request)
    if author_result[0]==False:
        print_errors(request, author_result[1])
        return redirect('book:editor')

    return redirect('book:show_book', new_book.id)
def print_errors(request, error_list):
    for error in error_list:
        message.add_message(request, messages.INFO, error)

def add_review(request, id):
    Review.objects.add_review(request, id)

    return redirect('book:show_book', id)

def show_book(request, id):
    context = {
        'book': Book.objects.get(id=id),
        'reviews': Review.objects.filter(reviewed_book=id)
    }

    return render(request, 'book_reviewer/show_book.html', context)

def show_user(request, id):
    pass

def destroy(request, review_id, book_id):
    Review.objects.destroy(request, review_id)

    return redirect('book:show_book', book_id)

def logout(request):
    request.session.clear()

    return redirect('login:index')
