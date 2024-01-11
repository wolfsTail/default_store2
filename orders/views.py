from django.contrib import messages
from django.db import transaction
from django.forms import ValidationError
from django.shortcuts import redirect, render

from carts.models import Cart
from orders.models import Order, OrderItem
from .forms import CreateOrderForm


def create_order(request):
    context = {}

    if request.method == "POST":
        form = CreateOrderForm(data=request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    user = request.user
                    cart_items = Cart.objects.filter(user=user)
                    if cart_items.exists():
                        order = Order.objects.create(
                            user=user,
                            phone_number=form.cleaned_data["phone_number"],
                            delivery_address=form.cleaned_data["delivery_address"],
                            requires_delivery=form.cleaned_data["requires_delivery"],
                            payment_on=form.cleaned_data["payment_on"],
                        )
                        for cart_item in cart_items:
                            product = cart_item.product
                            name = cart_item.product.name
                            price = cart_item.product.get_sell_price()
                            quantity = cart_item.quantity

                            if product.quantity < quantity:
                                raise ValidationError(f"Недостаточное количество товара: {name} в наличии на складе")
                            
                            OrderItem.objects.create(
                                order=order,
                                product=product,
                                name=name,
                                price=price,
                                quantity=quantity,
                            )
                            product.quantity -= quantity
                            product.save()
                        
                        cart_items.delete()

                        messages.success(request, "Заказ успешно оформлен, корзина обновлена!")
                        return redirect("user.profile")
            except ValidationError as err:
                messages.info(request, str(err))                
                return redirect("user.profile")   
    else:
        initial = {
            "first_name": request.user.first_name,
            "last_name": request.user.last_name,            
        }
        form = CreateOrderForm(initial=initial)

    context.update({
        "title": 'Оформление заказа',
        "form": form,
    })
    return render(request, "orders/create_order.html", context=context)
