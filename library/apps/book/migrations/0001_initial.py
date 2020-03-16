# Generated by Django 3.0.3 on 2020-03-16 18:28

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='BookPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=150, verbose_name='Book Name')),
                ('book_desc', models.TextField()),
                ('book_cover', models.ImageField(upload_to=None)),
                ('book_crt_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('book_pub_date', models.DateTimeField(blank=True, null=True)),
                ('book_author', models.ManyToManyField(to='book.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_author', models.CharField(max_length=150, verbose_name='Author of comment')),
                ('comment_text', models.CharField(max_length=200, verbose_name='Author of comment')),
                ('comment_pub', models.DateTimeField(verbose_name='Date of comment publishing')),
                ('book_page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.BookPage')),
            ],
        ),
        migrations.AddField(
            model_name='bookpage',
            name='book_genre',
            field=models.ManyToManyField(to='book.Genre'),
        ),
    ]
