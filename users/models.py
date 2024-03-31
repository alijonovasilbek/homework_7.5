from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    username = models.CharField(unique=True, max_length=100)
    email = models.EmailField(unique=True)
    birth_date = models.DateField(blank=True, null=True)
    email_confirmed = models.BooleanField(default=False)
    REQUIRED_FIELDS = [email, username]
