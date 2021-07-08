from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

class Books(models.Model):
    book = models.CharField(max_length=128)
    description = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)