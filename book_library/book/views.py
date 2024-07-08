from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def book(request):
    template = loader.get_template('book.html')
    return HttpResponse(template.render())


