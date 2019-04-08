from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_SuperUser = models.BooleanField(default=False)
    is_Just_User = models.BooleanField(default=False)
    is_SpecificUser = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class Account(models.Model):
    account_number = models.CharField(max_length=15, primary_key=True)
    name = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=11)
    amount = models.DecimalField(max_digits=20, decimal_places=4)
    created_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.account_number


class TopUP(models.Model):
    topup_account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='TopUP_Account')
    amount = models.DecimalField(max_digits=20, decimal_places=4)
    transection_time = models.DateTimeField(default=timezone.now)


class Payments(models.Model):
    payment_account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='payment_Account')
    amount = models.DecimalField(max_digits=20, decimal_places=4)
    transection_time = models.DateTimeField(default=timezone.now)


class CreditCard(models.Model):
    card_account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='Credit_card_Account')
    amount = models.DecimalField(max_digits=20, decimal_places=4)
    transection_time = models.DateTimeField(default=timezone.now)
