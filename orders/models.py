from django.db import models

from goods.models import Products
from users.models import User


class Order(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.SET_DEFAULT,
        default=None,
        verbose_name="Пользователь",
        blank=True,
        null=True,
    )
    created_timestamp = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата и время создания заказа"
    )
    phone_number = models.CharField(max_length=20, verbose_name="Номер телефона")
    delivery_address = models.TextField(
        null=True, blank=True, verbose_name="Адрес доставки"
    )
    requires_delivery = models.BooleanField(
        default=False, verbose_name="Необходимость доставки?"
    )
    payment_on = models.BooleanField(
        default=False, verbose_name="Оплата при получении?"
    )

    is_paid = models.BooleanField(default=False, verbose_name="Оплачен?")

    status = models.CharField(
        max_length=32,
        default="В обработке",
        verbose_name="Статус заказа",
    )

    class Meta:
        db_table = "order"
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
        ordering = ["-created_timestamp"]

    def __str__(self):
        return f"Заказ No{self.id} | Покупатель {self.user.email}"


class OrderItemsQuerySet(models.QuerySet):
    def get_total_price(self):
        return sum(item.products_price() for item in self)
    
    def total_quantity(self):
        if self:
            return sum(item.quantity for item in self)
        return 0


class OrderItem(models.Model):
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE, verbose_name="Заказ")
    product = models.ForeignKey(
        to=Products,
        on_delete=models.SET_DEFAULT,
        null=True,
        default=None,
        verbose_name="Продукт",
    )
    name = models.CharField(max_length=128, verbose_name="Наименование")
    price = models.DecimalField(
        max_digits=8, decimal_places=2, verbose_name="Стоимость"
    )
    quantity = models.PositiveIntegerField(default=0, verbose_name="Количество")
    created_timestamp = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата и время продажи"
    )
    objects = OrderItemsQuerySet.as_manager()

    class Meta:
        db_table = "order_item"
        verbose_name = "Товар в заказе"
        verbose_name_plural = "Товары в заказе"
        ordering = ["-created_timestamp"]
    
    def products_price(self):
        return round(self.price * self.quantity, 2)
    
    def __str__(self):
        return f"Заказ No{self.order.id} | Товар: {self.name}"
