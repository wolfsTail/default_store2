from django.shortcuts import render

from .models import Categories, Products


def catalog(request):
    context = {}
    goods = Products.objects.filter(quantity__gt=0)
    context.update(
        {'title': 'Default Store - Каталог',
        'goods': goods,}
    )
    return render(request, "goods/catalog.html", context)


def product(request):
    return render(request, "goods/product.html")
