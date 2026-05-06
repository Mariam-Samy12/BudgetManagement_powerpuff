from django.db import models
# from django.contrib.auth.models import User
from django.conf import settings
from django.core.exceptions import ValidationError

class Budget(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
    alert_threshold = models.IntegerField(default=80) 

    def __str__(self):
        return f"{self.category} Budget - {self.amount}"