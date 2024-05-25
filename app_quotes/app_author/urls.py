from . import views

from django.urls import path

from .views import AuthorListView, AuthorView

app_name = "app_author"

urlpatterns = [
    path("list/", AuthorListView.as_view(), name="author_list"),
    path("<int:pk>/", AuthorView.as_view(), name="author_edit_delete"),
    path(
        "<str:author_name>/", views.get_author, name="author_detail"
    ),  # Связано с формированием ссылки детально по автору из app_quotes.urls
    # path("", views.get_all, name="authors1"),
    path("", AuthorView.as_view(), name="author_add"),
]

# handler404 = "app_author.views.custom_404_view"  # Путь к вашей пользовательской функции обработчика ошибок 404
