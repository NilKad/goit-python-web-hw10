from . import views

from django.urls import path


app_name = "app_author"

urlpatterns = [
    path("", views.get_all, name="authors"),
    path("<str:author_name>/", views.get_author, name="author_detail"),
]

# handler404 = "app_author.views.custom_404_view"  # Путь к вашей пользовательской функции обработчика ошибок 404
