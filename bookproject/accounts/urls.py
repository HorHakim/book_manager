from django.urls import path


from . import views

app_name = 'accounts'
urlpatterns = [
		path("signup", views.signup, name="signup"),
  		path('login/', views.CustomLoginView.as_view(), name='login'),
		path('logout/', views.logout_to_book_library, name='logout'),
]