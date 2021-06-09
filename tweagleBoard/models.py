from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date

class Post(models.Model):
    title = models.CharField(max_length=500)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    post_time = models.TimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='tweag_posts')

    def __str__(self):
        return self.title + '|' + str(self.author)


# Create your models here.
