from django.db import models
from django.utils import timezone

class Author(models.Model):
	name = models.CharField(max_length=100, primary_key=True)
	STYLE_CHOICES = (("drama", "drama"), ("fiction", "fiction"), ("casual", "casual"), ("polar", "polar"))
	style = models.CharField(max_length=20, choices=STYLE_CHOICES)

	def __str__(self):
		return self.name

# Create your models here.
class Book(models.Model):
	title = models.CharField(max_length=200, primary_key=True)
	publication_date = models.DateField()
	author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

