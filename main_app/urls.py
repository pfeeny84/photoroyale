from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('accounts/signup/', views.signup, name='signup'),
    path('threads/', views.threads_index, name='index'),
    path('threads/create', views.ThreadCreate.as_view(), name='thread_create'),
    path('threads/<int:thread_id>/posts/', views.thread_posts_index, name='thread_posts_index'),
    path('genres/<int:pk>/delete/', views.ThreadDelete.as_view(), name='thread_delete'),
]