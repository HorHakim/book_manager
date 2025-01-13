from django.urls import path

from . import views

urlpatterns = [path("", views.show_books_list, name="books_list"),
			   path("add_book", views.add_book, name="add_book"),
			   path("<int:book_id>", views.book_details, name="book_details")
]