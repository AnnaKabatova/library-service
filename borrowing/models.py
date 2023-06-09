from django.db import models

from books.models import Book
from user.models import User


class Borrow(models.Model):
    borrow_date = models.DateField(auto_now_add=True)
    expected_return = models.DateField()
    actual_return = models.DateField(blank=True, null=True)
    book = models.ForeignKey(Book, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return f"{self.user.email}: {self.book.title}"
