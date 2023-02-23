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
from django.db.models import Q #Q Objects allows for multiple queries


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

class PostSearchView(ListView):
    template_name = "posts/search.html"
    model = Post

    def get_queryset(self): 
        # return Post.objects.filter(title__icontains='first')
        # (first test line, check server to see if filter is working)
        
        # return Post.objects.filter(
        #     Q(title__icontains='first') | 
        #     Q(subtitle__icontains='first') | 
        #     Q(body__icontains='first')
        # )
        #second test line, check to see if server is filtering multipe quieries
            
                    # only after testing multiple queries and adding the form to your nav bar or page add:

        query = self.request.GET.get("q")
        object_list = Post.objects.filter(
            Q(title__icontains=query) | Q(subtitle__icontains=query) | Q(body__icontains=query)
        )
        return object_list
        # (first test line to see if filter is working)
    
    #MVP Minimum Viable Product# Create your views here.
