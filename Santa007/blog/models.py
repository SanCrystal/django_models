from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    Author = models.ForeignKey(get_user_model() , on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    publish_date = models.DateTimeField(blank=True, null=True)

    def __repr__(self):
        return f'Title: {self.title} Author:  {self.Author}'