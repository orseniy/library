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


class book_page(models.Model):
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




class comment(models.Model):
    pass
