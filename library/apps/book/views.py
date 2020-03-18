from django.shortcuts import render
from .models import BookPage, Genre, Author, Comment

def index(request):
    latest_books_list = BookPage.objects.order_by('-book_pub_date')[:5]
    return render(request, 'book/list.html', {'latest_books_list':latest_books_list})

