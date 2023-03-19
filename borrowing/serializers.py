from typing import Dict, Any

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from borrowing.models import Borrow
from books.models import Book


class BorrowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrow
        fields = ("book", "expected_return")

    def create(self, validated_data: Dict[str, Any]) -> Borrow:
        book_update = Book.objects.get(title=validated_data["book"])
        if book_update.inventory > 0:
            book_update.inventory -= 1
            book_update.clean_inventory()
            book_update.save()
            return super().create(validated_data)
        raise ValidationError("This book is unavailable")


class BorrowListSerializer(BorrowSerializer):
    book = serializers.CharField(source="book.title")
    user = serializers.CharField(source="user.email")

    class Meta:
        model = Borrow
        fields = "__all__"


class BorrowReturnSerializer(serializers.ModelSerializer):
    book = serializers.CharField(source="book.title")

    class Meta:
        model = Borrow
        fields = ("book",)