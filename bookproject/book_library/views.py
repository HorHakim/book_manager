from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookForm
from .models import Book

# Create your views here.
def show_books_list(request):
	books = Book.objects.all().order_by('publication_date')
	return render(request, "book_library/books_list.html", {"books": books})

def add_book(request):
	if request.method == "GET":
		book_form = BookForm()
	elif request.method == "POST":
		book_form = BookForm(request.POST)
		if book_form.is_valid():
			book_form.save()
			return redirect("books_list")

	return render(request, "book_library/add_book.html", {"book_form" : book_form})

def book_details(request, book_id):
	book = get_object_or_404(Book, id=book_id)
	return render(request,  "book_library/book_details.html", {"book": book})