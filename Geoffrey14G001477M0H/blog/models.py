from cgitb import text
import datetime
from turtle import title
from unicodedata import name
from unittest.util import _MAX_LENGTH
from xmlrpc.client import DateTime
from django.db import models

# Create your models here.
class Post (models.Model):
    title = models.CharField (max_length = 200)
    text = models.TextField ()
    author = models.get_user_model ()
    Created_date = models.DateTimeField(DateTime)
    Published_date = models.DateTimeField(DateTime)

    



