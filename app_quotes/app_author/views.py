import re
from django.shortcuts import render, get_object_or_404
from .models import Author
from django.http import Http404

# Create your views here.


def convert_link_to_fullname(name):
    parts = name.split("-")
    result = ""
    for i in range(len(parts)):
        if len(parts[i]) <= 2:
            result += parts[i] + "."
            if len(parts) > (i + 1) and len(parts[i + 1]) > 2:
                result += " "
        else:
            result += parts[i] + " "
    result = result.strip()
    print(f"result: {result}")
    return result





def get_author(request, author_name=None):
    fullname = convert_link_to_fullname(author_name)
    print(f"{author_name} -> {fullname}")
    author = get_object_or_404(Author, fullname=fullname)
    print(author.fullname)

    return render(request, "app_author/author.html", context={"author": author})


def get_all(request):
    authors = Author.objects.all()
    # for author in authors:
        # author.detail_url = convert_fullname_to_link(author.fullname)
    return render(request, "app_author/authors.html", context={"authors": authors})


# def custom_404_view(request, exception):
#     return render(
#         request, "app_author/404.html", status=404, context={"exception": exception}
#     )
