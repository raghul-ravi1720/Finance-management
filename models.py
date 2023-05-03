from django.db import models
from django.contrib.auth.models import User
#from .models import Society, Member
from django.views.generic import ListView
#from .models import Transaction


class Society(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    email = models.EmailField()


class Member(models.Model):
    society = models.ForeignKey(Society, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    SHARE_CHOICES = (
        ('100', '100'),
        ('200', '200'),
        ('300', '300'),
        ('400', '400'),
    )
    share_number = models.CharField(max_length=100, choices=SHARE_CHOICES)


class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    society = models.ForeignKey(Society, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    CATEGORY_CHOICES = (
        ('deposit', 'Deposit'),
        ('withdrawl', 'Withdrawl'),
    )
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)

