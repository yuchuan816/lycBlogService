from django.db import models
from datetime import datetime
# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=20)
    body = models.TextField()
    created_time = models.DateTimeField(default=datetime.now)
    modified_time = models.DateTimeField(default=datetime.now)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.title
