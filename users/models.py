from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=150, unique=True, error_messages={"unique": "A user with that username already exists."})
    email = models.EmailField(max_length=127, unique=True, error_messages={"unique": "This field must be unique."})
