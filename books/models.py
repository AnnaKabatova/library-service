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

    @property
    def out_of_books(self) -> bool:
        return self.inventory == 0

    def __str__(self) -> str:
        return self.title
