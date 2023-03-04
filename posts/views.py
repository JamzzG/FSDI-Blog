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
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)  
    
from django.db.models import Q #Q Objects allows for multiple queries


class PostListView(ListView):
    template_name = "posts/list.html"
    model = Post


class PostDetailView(DetailView):
    template_name = "posts/detail.html"
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = "posts/new.html"
    model = Post
    fields = ["title", "subtitle", "body", "active"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin,  UserPassesTestMixin, UpdateView):
    model = Post
    template_name = "posts/edit.html"
    fields = ["title", "subtitle", "body", "active"]

    def test_func(self):
        user = self.request.user
        post = self.get_object()
        return user == post.author
    

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = "posts/delete.html"
    model = Post
    success_url = reverse_lazy("list")

    def test_func(self):
        user = self.request.user
        post = self.get_object()
        return user == post.author
        

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
