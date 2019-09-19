from django.db import models
from django.contrib.auth.models import User
from article.models import Article
from django.utils import timezone


# Create your models here.
class Comment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(
        Article, null=True, blank=True, related_name='comments', on_delete=models.CASCADE)
    comments = models.ForeignKey(
        'self', null=True, blank=True, related_name='reply', on_delete=models.CASCADE)
    created_time = models.DateTimeField(default=timezone.now)
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.content


class CommentLikeAndOpposition(models.Model):
    TYPE = (
        (0, '点赞'),
        (1, '反对'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    type = models.IntegerField(null=True, choices=TYPE)
