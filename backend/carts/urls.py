from django.urls import path
from . import views


app_name = "carts"

urlpatterns = [
    path("cart_add/", views.cart_add, name="cart_add"),
    path("cart_remove/", views.cart_remove, name="cart_remove"),
    path("cart_update/", views.cart_update, name="cart_update"),
]
