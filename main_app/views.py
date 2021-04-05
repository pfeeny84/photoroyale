from django.shortcuts import render, redirect
from .models import Thread, Post, Comment, Image
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.contenttypes.models import ContentType

# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


class ThreadCreate(CreateView):
    model = Thread
    fields = ['title', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ThreadDelete(DeleteView):
    model = Thread
    success_url = '/'


class ThreadUpdate(UpdateView):
    model = Thread
    fields = ['description']


def threads_index(request):
    threads = Thread.objects.all()
    return render(request, 'threads/index.html', {'threads': threads})


def thread_posts_index(request, thread_id):
    posts = Post.objects.filter(thread=thread_id)
    thread = Thread.objects.get(id=thread_id)

    contenttype_obj = ContentType.objects.get_for_model(thread)
    image = Image.objects.filter(object_id=thread.id, content_type=contenttype_obj).first().url

    fullposts = []
    for post in posts:
      contenttype_obj_post = ContentType.objects.get_for_model(posts.first())
      post_image = Image.objects.filter(object_id=posts.first().id, content_type=contenttype_obj_post).first().url
      fullposts.append({'post': post, 'image': post_image})

    return render(request, 'threads/posts/index.html', {'posts': fullposts, 'thread': thread, 'url': image,})


class PostCreate(CreateView):
    model = Post
    fields = []

    def form_valid(self, form):
        form.instance.user = self.request.user
        print(self.kwargs['thread_id'], 'this is self.kwargs')
        form.instance.thread = Thread.objects.get(id=self.kwargs['thread_id'])
        return super().form_valid(form)


class PostDelete(DeleteView):
    model = Post
    success_url = '/threads/'


class PostUpdate(UpdateView):
    model = Post
    fields = []


def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    comments = Comment.objects.filter(post=post_id)

    contenttype_obj = ContentType.objects.get_for_model(post)
    image = Image.objects.filter(object_id=post.id, content_type=contenttype_obj).first().url

    return render(request, 'threads/posts/detail.html', {'post': post, 'comments': comments, 'url': image})


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'

    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


class CommentCreate(CreateView):
  model = Comment
  fields = ['content']

  def form_valid(self, form):
    form.instance.user = self.request.user
    form.instance.post = Post.objects.get(id=self.kwargs['post_id'])
    return super().form_valid(form)


class CommentDelete(DeleteView):
  model = Comment
  success_url = '/threads/'


class CommentUpdate(UpdateView):
  model = Comment
  fields = ['content']


