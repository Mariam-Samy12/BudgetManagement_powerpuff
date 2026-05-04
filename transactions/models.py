from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('income', 'Income'),
        ('expense', 'Expense'),
    ]

    PAYMENT_METHODS = [
        ('cash', 'Cash'),
        ('credit_card', 'Credit Card'),
        ('bank_transfer', 'Bank Transfer'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50)
    type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    date = models.DateTimeField(default=timezone.now) 
    description = models.TextField(max_length=200, blank=True, null=True)
    payment_method = models.CharField(
        max_length=50, 
        choices=PAYMENT_METHODS, 
        blank=True, 
        null=True
    )

    def __str__(self):
        return f"{self.user.username} - {self.category} ({self.amount})"