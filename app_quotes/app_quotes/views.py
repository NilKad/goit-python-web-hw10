import re
from django.urls import reverse_lazy
from django.shortcuts import render, HttpResponse, redirect
from django.core.paginator import Paginator
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse
from .models import Quote
from .forms import QuoteForm


def convert_fullname_to_link(name):
    result = re.sub(r"\.\s|\s|\.", "-", name)
    # print(f"result: '{result}'")
    return result


def index(request):
    quotes = Quote.objects.order_by("id").all()
    page_number = request.GET.get("page")
    per_page = request.GET.get("per_page")
    print(f"GET {request.path}")
    print(f"GET {request.path_info}")
    if not per_page:
        per_page = 10
    is_edit = False
    if request.path == "/quotes/":
        is_edit = True
        per_page = 30
    paginator = Paginator(quotes, per_page)

    # Создание ссылки для старницы автора из fullname
    for quote in quotes:
        quote.tags = quote.tags.split(",")
        fullname_uri = convert_fullname_to_link(quote.author.fullname)
        quote.author_detail_url = f"author/{fullname_uri}"

    page_obj = paginator.get_page(page_number)

    if is_edit:
        return render(request, "app_quotes/quotes_list.html", {"page_obj": page_obj})
    else:
        return render(request, "app_quotes/index.html", {"page_obj": page_obj})


class QuoteUpdateView(UpdateView):
    model = Quote
    form_class = QuoteForm
    template_name = "app_quotes/quoute_form.html"
    success_url = reverse_lazy("quote_list")


class QuoteDeleteView(DeleteView):
    model = Quote
    template_name = "app_quotes/quote_confirm_delete.html"
    success_url = reverse_lazy("quote_list")


def custom_404_view(request, exception):
    return render(
        request, "app_quotes/404.html", status=404, context={"exception": exception}
    )
