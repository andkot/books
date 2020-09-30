from django.db import models


class Book(models.Model):
    title = models.CharField(verbose_name='Title', max_length=255)
    author_name = models.CharField(verbose_name='Author name', max_length=255)
    description = models.TextField(verbose_name='Description')
