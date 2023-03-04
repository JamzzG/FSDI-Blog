from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)  
from django.urls import reverse_lazy


class SignUpView(CreateView):
    template_name = "registration/signup.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("login")

class ChangePasswordView(PasswordChangeForm):
    template_name = "registration/password_change_form.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("password_change_done.html")

    def test_func(self):
        user = self.request.user
        post = self.get_object()
        return user ==  'posts.Post.author'

class PasswordChangedView(DetailView):
    model =  'posts.Post'
    template_name = "registration/password_change_done.html"



# Create your views here.
