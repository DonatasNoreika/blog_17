from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .models import Post
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
class PostListView(generic.ListView):
    model = Post
    template_name = "posts.html"
    context_object_name = "posts"


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "post.html"
    context_object_name = 'post'


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    template_name = "signup.html"
    success_url = reverse_lazy("login")