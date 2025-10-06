from django.shortcuts import render
from django.views import generic
from .models import Book

# Create your views here.
class BookList(generic.ListView):
    queryset = Book.objects.all()
    template_name = "library/library_list.html"