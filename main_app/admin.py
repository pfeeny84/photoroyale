from django.contrib import admin
from .models import Image, Thread, Post, Comment, ThreadImage, PostImage, ProfileImage

# Register your models here.
admin.site.register(Image)
admin.site.register(Thread)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(ThreadImage)
admin.site.register(PostImage)
admin.site.register(ProfileImage)