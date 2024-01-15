from django.shortcuts import render
from django.http import HttpResponse

from main.models import (
    IndexPageContent,
    AboutPageContent,
    PayAndDeliveryPageContent,
    InformationPageContent,
)


def index(request):
    context = {}
    try:
        actual_content = IndexPageContent.objects.latest("created_timestamp")
        context.update(
            {
                "title": actual_content.title,
                "content": actual_content.content,
            }
        )
    except:
        context.update(
            {
                "title": "Default Store - Index",
                "content": "Empty blank 2.0. Use admin panel to create content!",
            }
        )
    return render(request, "main/index.html", context)


def about(request):
    context = {}
    try:
        actual_content = AboutPageContent.objects.latest("created_timestamp")
        context.update(
            {
                "title": actual_content.title,
                "content": actual_content.content,
                "text_on_page": actual_content.text_in_page,
            }
        )
    except:
        context.update(
            {
                "title": "Default Store - About",
                "content": "Use admin panel to create content on 'about' page!",
                "text_on_page": "Empty blank.",
            }
        )
    return render(request, "main/about.html", context)


def pay_and_delivery(request):
    context = {}
    try:
        actual_content = PayAndDeliveryPageContent.objects.latest("created_timestamp")
        context.update(
            {
                "title": actual_content.title,
                "content": actual_content.content,
                "text_on_page": actual_content.text_in_page,
            }
        )
    except:
        context.update(
            {
                "title": "Default Store - Pay & Delivery",
                "content": "Use admin panel to create content on 'P&D' page!",
                "text_on_page": "Empty blank.",
            }
        )
    return render(request, "main/pay_and_delivery.html", context)


def information(request):
    context = {}
    try:
        actual_content = InformationPageContent.objects.latest("created_timestamp")
        context.update(
            {
                "title": actual_content.title,
                "content": actual_content.content,
                "text_on_page": actual_content.text_in_page,
            }
        )
    except:
        context.update(
            {
                "title": "Default Store - Information",
                "content": "Use admin panel to create content on 'information' page!",
                "text_on_page": "Empty blank.",
            }
        )
    return render(request, "main/information.html", context)
