import re
from django.shortcuts import render, HttpResponse, redirect
from django.core.paginator import Paginator
from django.urls import reverse
from .models import Quote


def convert_fullname_to_link(name):
    result = re.sub(r"\.\s|\s|\.", "-", name)
    print(f"result: '{result}'")
    return result


def index(request):
    quotes = Quote.objects.all()
    page_number = request.GET.get("page")
    # per_page = request.GET.get("per_page")
    per_page = 10
    paginator = Paginator(quotes, per_page)
    for quote in quotes:
        quote.tags = quote.tags.split(",")
        fullname_uri = convert_fullname_to_link(quote.author.fullname)
        # quote.author_detail_url = reverse(
        #     "app_author:author_detail", args=[fullname_uri]
        # )
        quote.author_detail_url = f"author/{fullname_uri}"

    page_obj = paginator.get_page(page_number)

    return render(request, "app_quotes/index.html", {"page_obj": page_obj})


def custom_404_view(request, exception):
    return render(
        request, "app_quotes/404.html", status=404, context={"exception": exception}
    )
