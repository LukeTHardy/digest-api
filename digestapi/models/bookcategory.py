from django.db import models


class BookCategory(models.Model):
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name='categories')
    book = models.ForeignKey("Book", on_delete=models.CASCADE, related_name='books')
    date = models.DateField()