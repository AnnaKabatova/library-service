from django.db import models


class Book(models.Model):
    class Enum(models.IntegerChoices):
        HARD = 0
        SOFT = 1

    title = models.CharField(max_length=100)
    author = models.CharField(max_length=63)
    cover = models.BooleanField(choices=Enum.choices)
    inventory = models.PositiveIntegerField()
    daily_fee = models.DecimalField(max_digits=5, decimal_places=2)
    out_of_books = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title

    def clean_inventory(self) -> None:
        if self.inventory == 0:
            self.out_of_books = True
