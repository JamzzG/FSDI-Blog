from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=128)
    subtitle = models.CharField(max_length=128)
    author = models.ForeignKey(
        'auth.User',
        #model responsible for creating users
        on_delete=models.CASCADE
        #if users are deleted so will all their posts.
    )
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("detail", args=[self.id])