from django.shortcuts import render, redirect
from .models import Thread, Post, Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


class ThreadCreate(LoginRequiredMixin, CreateView):
    model = Thread
    fields = ['title', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ThreadDelete(LoginRequiredMixin, DeleteView):
    model = Thread
    success_url = '/'


class ThreadUpdate(LoginRequiredMixin, UpdateView):
    model = Thread
    fields = ['description']


def threads_index(request):
    threads = Thread.objects.all()
    return render(request, 'threads/index.html', {'threads': threads})


def thread_posts_index(request, thread_id):
    posts = Post.objects.filter(thread=thread_id)
    thread = Thread.objects.get(id=thread_id)
    return render(request, 'threads/posts/index.html', {'posts': posts, 'thread': thread})


class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = []

    def form_valid(self, form):
        form.instance.user = self.request.user
        print(self.kwargs['thread_id'], 'this is self.kwargs')
        form.instance.thread = Thread.objects.get(id=self.kwargs['thread_id'])
        return super().form_valid(form)


class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post

    def get_object(self, queryset = None):
        thread = self.kwargs['thread_id']
        print(thread)
    success_url = '/threads/'


class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    fields = []

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    comments = Comment.objects.filter(post=post_id)
    return render(request, 'threads/posts/detail.html', {'post': post, 'comments': comments})


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


class CommentCreate(LoginRequiredMixin, CreateView):
  model = Comment
  fields = ['content']

  def form_valid(self, form):
    form.instance.user = self.request.user
    form.instance.post = Post.objects.get(id=self.kwargs['post_id'])
    return super().form_valid(form)


class CommentDelete(LoginRequiredMixin, DeleteView):
  model = Comment
  success_url = '/threads/'


class CommentUpdate(LoginRequiredMixin, UpdateView):
  model = Comment
  fields = ['content']


