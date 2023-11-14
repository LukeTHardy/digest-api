from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    book = models.ForeignKey("Book", on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField(null=True, blank=True)
    comments = models.CharField(max_length=155)
    date = models.DateTimeField(default=timezone.now)
