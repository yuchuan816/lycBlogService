from django.db import models

# Create your models here.


class Student(models.Model):
    FEMALE = 0
    MALE = 1
    SEX_CHOICES = (
        (FEMALE, '女'),
        (FEMALE, '男')
    )

    name = models.CharField(max_length=20)
    sex = models.IntegerField(choices=SEX_CHOICES, default=1)
    age = models.IntegerField()
    content = models.CharField(max_length=40)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.name
