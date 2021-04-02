from django.shortcuts import render, redirect
from .models import Thread
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views.generic.edit import CreateView

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

class ThreadCreate(CreateView):
  model = Thread
  fields = '__all__'
  
#   def form_valid(self, form):
#     form.instance.user = self.request.user
#     return super().form_valid(form)

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

def threads_index(request):
    threads = Thread.objects.filter(user=request.user)
    return render(request, 'threads/index.html', { 'threads': threads })