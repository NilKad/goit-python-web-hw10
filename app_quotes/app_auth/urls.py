from . import views
from django.urls import path
from django.contrib.auth.views import LoginView

from .forms import LoginForm

app_name = "app_auth"

urlpatterns = [
    path("signup/", views.RegisetrView.as_view(), name="signup"),
    path(
        "signin/",
        LoginView.as_view(
            template_name="app_auth/login.html",
            form_class=LoginForm,
            redirect_authenticated_user=True,
        ),
        name="signin",
    ),
    path(
        "logout/",
        views.CustomLogoutView.as_view(template_name="app_auth/logout.html"),
        name="logout",
    ),
]
