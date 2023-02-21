from django.views.generic import (
    DetailView,
    ListView,
)
from django.views.generic.edit import(
    CreateView,
    DeleteView,
    UpdateView,
)


from .models import Post
from django.urls import reverse_lazy


class PostListView(ListView):
    template_name = "posts/list.html"
    model = Post


class PostDetailView(DetailView):
    template_name = "posts/detail.html"
    model = Post


class PostCreateView(CreateView):
    template_name = "posts/new.html"
    model = Post
    fields = ["title", "subtitle", "author", "body", "active"]


class PostUpdateView(UpdateView):
    model = Post
    template_name = "posts/edit.html"
    fields = ["title", "subtitle", "body", "active"]
    

class PostDeleteView(DeleteView):
    template_name = "posts/delete.html"
    model = Post
    success_url = reverse_lazy("list")

    
    
    #MVP Minimum Viable Product# Create your views here.
