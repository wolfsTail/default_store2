from django.shortcuts import render
from django.http import HttpResponse

from goods.models import Categories


def index(request):
    context = {}
    categories = Categories.objects.all()
    context.update(
        {
            "title": "Default Store - Главная",
            "content": "Default shop blank 2.0",
            "categories": categories,
        }
    )
    return render(request, "main/index.html", context)


def about(request):
    context = {}
    context.update(
        {
            "title": "Default Store - О нас",
            "content": "Коротко о нас!",
            "text_on_page": "Заглушка информацию о сайте.",
        }
    )
    return render(request, "main/about.html", context)


def pay_and_delivery(request):
    context = {}
    context.update(
        {
            "title": "Default Store - Оплата и доставка",
            "content": "Оплата и доставка",
            "text_on_page": "Заглушка о способах оплаты и доставки.",
        }
    )
    return render(request, "main/pay_and_delivery.html", context)


def information(request):
    context = {}
    context.update(
        {
            "title": "Default Store - Контактная информация",
            "content": "Контактная информация",
            "text_on_page": "Заглушка для страницы информации о сайте.",
        }
    )
    return render(request, "main/information.html", context)
