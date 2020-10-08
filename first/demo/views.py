from django.http import request
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Book


# Create your views here.


def first(request):
    return HttpResponse('First')


class Another(View):

    books = Book.objects.all()
    output = ''

    for book in books:
        #print(output)
        output += f"we hav {book.title} that books in DB <br>"

    def get(self, request):
      return HttpResponse(self.output)