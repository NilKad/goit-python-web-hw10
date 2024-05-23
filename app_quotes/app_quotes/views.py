from django.shortcuts import render, HttpResponse, redirect


def index(request):
    return render(
        request,
        "app_quotes/index.html",
        context={
            "msg": "Hello world!!!!!!!",
        },
    )
