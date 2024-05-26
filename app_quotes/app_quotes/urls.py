"""
URL configuration for app_quotes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from . import views
from app_author.views import get_all

from django.contrib import admin
from django.urls import path, include
from .views import QuoteUpdateView

app_name = "app_quotes"

urlpatterns = [
    path("", views.index, name="home"),
    path("quotes/", views.index, name="quote_list"),
    path("quotes/add", views.index, name="quote_add"),
    path("quotes/edit/<int:pk>", QuoteUpdateView.as_view(), name="quote_edit"),
    path("quotes/del/<int:pk>", views.index, name="quote_delete"),
    path("author/", include("app_author.urls"), name="author"),
    path("admin/", admin.site.urls),
]

handler404 = "app_quotes.views.custom_404_view"  # Путь к вашей пользовательской функции обработчика ошибок 404
