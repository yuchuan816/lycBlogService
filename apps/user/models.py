from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    name = models.CharField()
    age = models.IntegerField()
    gender = models.CharField()

    def __str__(self):
        return self.name