from django.db import models

# Create your models here.
from common.models import BaseModel


class Author(BaseModel):
    name = models.CharField(max_length=32)


class Book(BaseModel):
    name = models.CharField(max_length=32)
    author = models.ForeignKey('books.Author', on_delete=models.SET_DEFAULT, default='')
