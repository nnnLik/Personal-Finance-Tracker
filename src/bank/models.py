from django.db import models

from django.conf import settings


class Bank(models.Model):
    """
    Users bank model
    """

    name = models.CharField(max_length=50, blank=False, null=False)
    description = models.TextField(blank=True, null=True, max_length=200)
    money = models.BigIntegerField(default=0)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_bank"
    )
    transaction = models.ForeignKey(
        "Transaction", on_delete=models.CASCADE, related_name="transaction_bank"
    )


class Category(models.Model):
    """
    Category model for transactions
    """

    name = models.CharField(max_length=50, blank=False, null=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="which_category",
    )


class Transaction(models.Model):
    """
    Transaction model for each users bank
    """

    amount = models.PositiveBigIntegerField(
        verbose_name="transaction amount", blank=False, null=False
    )
    category = models.ForeignKey(
        "Category",
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        verbose_name="category_of_transaction",
    )
    date_execution = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    bank = models.ForeignKey(
        "Bank",
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name="transactions_bank",
    )  # TODO: on delete instead of SET_NULL use SET and take the name of deleted bank
