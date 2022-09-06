from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the webshop_app index.")
