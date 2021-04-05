from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Models

class Image(models.Model):
    url = models.CharField(max_length=200)
    
class ProfileImage(Image):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Thread(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('thread_posts_index', kwargs={'thread_id': self.id})

class ThreadImage(Image):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)

class Post(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'post_id': self.id})

    

class PostImage(Image):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

class Comment(models.Model):
    content = models.CharField(max_length=200)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'post_id': self.post.id})