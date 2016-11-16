from django.shortcuts import render, redirect
  # Create your views here.
def index(request):

    return render(request, "book_reviewer/index.html")

def add_book_and_review(request):
    pass

def add_review(request, id):
    pass

def show_book(request, id):
    pass

def show_user(request, id):
    pass

def destroy_review(request, id):
    pass

def logout(request):
    request.session.clear()

    return redirect('login:index')
