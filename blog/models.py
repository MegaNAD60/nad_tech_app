from django.db import models
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(blank=True)
    author = models.ForeignKey(
        'auth.User', 
        on_delete=models.CASCADE,
    )
    body = models.TextField()

    def __str__(self):
        return self.title

class PostImage(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.post.title 

