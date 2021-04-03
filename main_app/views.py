from django.shortcuts import render, redirect
from .models import Thread, Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views.generic.edit import CreateView, DeleteView

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

def threads_index(request):
    threads = Thread.objects.all()
    return render(request, 'threads/index.html', { 'threads': threads })

def thread_posts_index(request, thread_id):
    posts = Post.objects.filter(thread=thread_id)
    thread = Thread.objects.get(id=thread_id)
    return render(request, 'threads/posts/index.html', { 'posts': posts, 'thread':thread})














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
