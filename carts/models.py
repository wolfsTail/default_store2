from django.db import models

from goods.models import Products
from users.models import User


class CartQuerySet(models.QuerySet):
    def total_price(self):
        if self:
            return sum(item.products_price() for item in self)
        else:
            return 0
    
    def total_quantity(self):
        if self:
            return sum(item.quantity for item in self)
        else:
            return 0


class Cart(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True,verbose_name="Пользователь")
    product = models.ForeignKey(to=Products, on_delete=models.CASCADE, verbose_name="Товар")
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name="Количество")
    session_key = models.CharField(max_length=64, blank=True, null=True, verbose_name="Ключ сессии")
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Время добпвления товара")
    objects = CartQuerySet.as_manager()


    class Meta:
        db_table = "cart"
        verbose_name = "Корзину"
        verbose_name_plural = "Корзины"
        ordering = ["-created_timestamp"]
       
    
    def __str__(self) -> str:
        return f"Заказ: {self.user.username} | Товар: {self.product.name} | Кол-во: {self.quantity}"
    
    def products_price(self):
        return round(self.product.get_sell_price() * self.quantity, 2)
    