from django.db import models
from django.contrib.auth.models import User

# Models

class Image(models.Model):
    url = models.CharField(max_length=200)

class Thread(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class ThreadImage(Image):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)

class Post(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class PostImage(Image):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

class Comment(models.Model):
    content = models.CharField(max_length=200)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    


# Images
    

class ProfileImage(Image):
    user = models.ForeignKey(User, on_delete=models.CASCADE)