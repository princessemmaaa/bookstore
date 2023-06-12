from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Profile
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .forms import BookForm

@login_required
def book_edit(request, id):
    book = get_object_or_404(Book, id=id)
    if book.created_by != request.user:
        return HttpResponseForbidden("You can't edit someone else's book.")
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('books:book_detail', id=id)
    else:
        form = BookForm(instance=book)
    return render(request, 'books/book_edit.html', {'form': form})

@login_required
def book_delete(request, id):
    book = get_object_or_404(Book, id=id)
    if book.created_by != request.user:
        return HttpResponseForbidden("You can't delete someone else's book.")
    if request.method == 'POST':
        book.delete()
        return redirect('books:book_list')
    return render(request, 'books/book_confirm_delete.html', {'book': book})

#To resctict any functions to only authenticated users, use the following. 
#@login_required
#def book_detail(request, id):
    # your view logic here...

def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

@login_required
def book_detail(request, id):
    book = Book.objects.get(id=id)
    return render(request, 'books/book_detail.html', {'book': book})

def profile_list(request):
    profiles = Profile.objects.all()
    return render(request, 'books/profile_list.html', {'profiles': profiles})

def profile_detail(request, id):
    profile = get_object_or_404(Profile, id=id)
    return render(request, 'books/profile_detail.html', {'profile': profile})

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("books:book_list")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render (request=request, template_name="books/register.html", context={"register_form":form})

@login_required
def profile(request):
    return render(request, 'books/profile.html', {'user': request.user})

