from django.urls import path
from .views import (
    SignUpView,
    ChangePasswordView,
    PasswordChangedView,
)


urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    # path("change_password_form/", ChangePasswordView.as_view(), name="change_password"),
    # path("signup/", PasswordChangedView.as_view(), name="password_changed"),
]

