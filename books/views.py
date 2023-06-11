from django.shortcuts import render
from .models import Book

def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

def book_detail(request, id):
    book = Book.objects.get(id=id)
    return render(request, 'books/book_detail.html', {'book': book})