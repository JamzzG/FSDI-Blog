from django.urls import path
from .views import (
    PostListView,
    PostUpdateView,
    PostDeleteView,
    PostDetailView,
    PostCreateView,
    PostSearchView,
)

urlpatterns = [
    path("list/",PostListView.as_view(), name="list"),
    path("new/", PostCreateView.as_view(), name="new"),
    path("<int:pk>/edit/", PostUpdateView.as_view(), name="edit"),
    path("<int:pk>/delete/", PostDeleteView.as_view(), name="delete"),
    path("<int:pk>/", PostDetailView.as_view(), name="detail"),
    path("search/", PostSearchView.as_view(), name="search"),
]