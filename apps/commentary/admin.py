from django.contrib import admin
from .models import Comment, CommentLikeAndOpposition


# Register your models here.
admin.site.register(Comment)
admin.site.register(CommentLikeAndOpposition)
