from django.db import models

# Create your models here.
import uuid
from django.db import models
from django.conf import settings
from decimal import Decimal

class Customer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    credit_limit = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('500.00'))

    def __str__(self):
        return f"Customer: {self.user.username}"

class Transaction(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('COMPLETED', 'Completed'),
        ('FAILED', 'Failed'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, related_name='transactions')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')

class BNPLPlan(models.Model):
    STATUS_CHOICES = [
        ('ACTIVE', 'Active'),
        ('PAID', 'Paid'),
        ('DEFAULTED', 'Defaulted'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    transaction = models.OneToOneField(Transaction, on_delete=models.CASCADE, related_name='bnpl_plan')
    installments_total = models.IntegerField(default=3)
    remaining_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ACTIVE')