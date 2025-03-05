from django.db import models

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
    phone = models.CharField(max_length=15)
    address = models.TextField()
    membership_type = models.ForeignKey(SubscriptionPlan, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Active')

    def __str__(self):
        return self.name