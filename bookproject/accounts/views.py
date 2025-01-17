from django.shortcuts import render, redirect
from .forms import CustomSignUpForm
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.contrib import messages



# Create your views here.
def signup(request):
	if request.method == "GET":
		signup_form = CustomSignUpForm()
		
	elif request.method == "POST":
		signup_form = CustomSignUpForm(request.POST)
		if signup_form.is_valid():
			user = signup_form.save()
			login(request, user)
			return redirect("book_library:books_list")

	return render(request, "accounts/signup.html", {"signup_form" : signup_form})


class CustomLoginView(LoginView):
  template_name = 'accounts/login.html'
  next_page = 'book_library:books_list'

  def form_invalid(self, form):
      messages.error(self.request, "Invalid username or password")
      return super().form_invalid(form)






def logout_to_book_library(request):
    logout(request)
    return redirect("book_library:books_list")