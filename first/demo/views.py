from django.http import request
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.views import View

from .models import Book
from .serializers import BookSerializer, BookMiniSerializer

# Create your views here.
def first(request):
    books = Book.objects.all()

    return render( request, 'first_template.html', {'books' : books})


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookMiniSerializer
    queryset = Book.objects.all()
    authentication_classes= (TokenAuthentication,)
    permission_classes=(IsAuthenticated,)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = BookSerializer(instance)
        return Response(serializer.data)
