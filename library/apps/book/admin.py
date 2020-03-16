from django.contrib import admin
from .models import BookPage, Genre, Author, Comment

admin.site.register(BookPage)
admin.site.register(Genre)
admin.site.register(Author)
admin.site.register(Comment)

