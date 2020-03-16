from django.db import models
from django.conf import settings
from django.utils import timezone

class Genre(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class BookPage(models.Model):
    book_name = models.CharField('Book Name', max_length=150)
    book_desc = models.TextField()
    book_author = models.ManyToManyField(Author)
    book_cover = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100,) #FIX IT
    book_genre = models.ManyToManyField(Genre)
    book_crt_date = models.DateTimeField(default=timezone.now)
    book_pub_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()




class Comment(models.Model):
    book_page = models.ForeignKey(BookPage, on_delete= models.CASCADE)
    comment_author = models.CharField('Author of comment', max_length=150)
    comment_text = models.CharField('Comment text', max_length=200)
    comment_pub = models.DateTimeField('Date of comment publishing')
