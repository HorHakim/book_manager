from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookForm, AuthorForm
from .models import Book
from django.contrib.auth.decorators import login_required


# Create your views here.
def show_books_list(request):
	books = Book.objects.all().order_by('publication_date')
	return render(request, "book_library/books_list.html", {"books": books})


@login_required
def add_book(request):
	if request.method == "GET":
		book_form = BookForm()
	elif request.method == "POST":
		book_form = BookForm(request.POST)
		if book_form.is_valid():
			book_form.save()
			return redirect("book_library:books_list")

	return render(request, "book_library/add_book.html", {"book_form" : book_form})

@login_required
def add_author(request):
	if request.method == "GET":
		author_form = AuthorForm()
	elif request.method == "POST":
		author_form = AuthorForm(request.POST)
		if author_form.is_valid():
			author_form.save()
			return redirect("book_library:books_list")

	return render(request,"book_library/add_author.html", {"author_form" : author_form})



def book_details(request, book_title):
	book = get_object_or_404(Book, title=book_title)
	return render(request,  "book_library/book_details.html", {"book": book})