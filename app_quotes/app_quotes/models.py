from django.db import models


class Author(models.Model):
    fullname = models.CharField(max_length=255)
    born_date = models.CharField(max_length=255)
    born_location = models.CharField(max_length=255)
    description = models.TextField()


class Quote(models.Model):
    quote = models.TextField()
    tags = models.CharField(max_length=255)
    author = models.ForeignKey(Author, related_name='quotes', on_delete=models.CASCADE)


