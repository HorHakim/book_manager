from django.urls import path

from . import views

urlpatterns = [path("", views.show_books_list, name="books_list"),
			   path("add_book", views.add_book, name="add_book"),
			   path("add_author", views.add_author, name="add_author"),
			   path("<str:book_title>", views.book_details, name="book_details")
]