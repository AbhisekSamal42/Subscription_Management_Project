from django.db import models
from django.core.exceptions import ValidationError
import re

# Create your models here.

class SubscriptionPlan(models.Model):
    PLAN_TYPES = [
        ('Monthly', 'Monthly'),
        ('Quarterly', 'Quarterly'),
        ('Yearly', 'Yearly'),
    ]

    plan_name = models.CharField(max_length=100)
    duration = models.CharField(max_length=10, choices=PLAN_TYPES)
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.plan_name


class Member(models.Model):
    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Paused', 'Paused'),
        ('Deactivated', 'Deactivated'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=13)
    address = models.TextField()
    membership_type = models.ForeignKey(SubscriptionPlan, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Active')

    def clean(self):
            # Validate Name (Only alphabets and spaces)
        if not re.match(r'^[A-Za-z]+$',self.name):
            raise ValidationError({'name':'Name should contain only alphabets and spaces.'})
        
                # Validate Phone (Should start with +91 and a number starting with 6,7,8,9)
        if not re.match(r'^\+91[6789]\d{9}$', self.phone):
            raise ValidationError({'phone': 'Phone number must start with +91 and be followed by a 10-digit number starting with 6, 7, 8, or 9.'})
        
    def save(self, *args, **kwargs):
        self.full_clean()  
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name