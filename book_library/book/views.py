from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Book
def book2(request):
    template = loader.get_template('book.html')
    return HttpResponse(template.render())

def book(request):
    my_books = Book.objects.all().values
    template = loader.get_template('all_books.html')
    context = {
        'my_books': my_books,
    }
    return HttpResponse(template.render(context, request))


