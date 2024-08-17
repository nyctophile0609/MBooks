from django.db import models


class BooksModel(models.Model):
    title=models.CharField(max_length=250)
    author=models.CharField(max_length=150)
    language=models.CharField(max_length=150)
    topic=models.CharField(max_length=150)
    pages=models.PositiveIntegerField()
    published_date=models.DateField()
    book_link=models.URLField(blank=True,null=True)
    book_cover_link=models.URLField(blank=True,null=True)
    created_date=models.DateTimeField(auto_now_add=True)