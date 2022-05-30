from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    isEmailValid = models.BooleanField()
    country = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=50, null=True)
    district = models.CharField(max_length=50, null=True)
    zipcode = models.IntegerField(null=True)

