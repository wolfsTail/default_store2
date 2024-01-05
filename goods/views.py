from django.core.paginator import Paginator
from django.shortcuts import get_list_or_404, render

from .utils import q_search
from .models import Categories, Products


def catalog(request, category_slug=None):
    context = {}
    # get request params from url to apply filter's
    page = request.GET.get('page', 1)
    on_sale = request.GET.get('on_sale', None)
    order_by = request.GET.get('order_by', None)
    query = request.GET.get('q', None)
    #  get goods by params
    if category_slug == 'all':
        goods = Products.objects.all()
    elif query:
        goods = q_search(query)
    else:
        goods = get_list_or_404(Products.objects.filter(category__slug=category_slug))   
    # check filtres
    if on_sale:
        goods = goods.filter(discount__gt=0)
    if order_by and order_by != 'default':
        goods = goods.order_by(str(order_by))     
    # use pagination
    paginator = Paginator(goods, 3)
    current_page = paginator.page(int(page))

    context.update(
        {'title': 'Default Store - Каталог',
        'slug_url': category_slug,
        'goods': current_page,}
    )
    return render(request, "goods/catalog.html", context)


def product(request, product_slug=None, product_id=None):
    context = {}

    if product_slug:
        product = Products.objects.get(slug=product_slug)
    elif product_id:
        product = Products.objects.get(id=product_id)

    context.update(
        {'product': product,}
    )
    return render(request, "goods/product.html", context)
