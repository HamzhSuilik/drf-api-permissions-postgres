from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from .models import Books
from .serializers import BookSerializer

# Create your views here.

class BookList(ListCreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer

class BookDetail(RetrieveUpdateAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer