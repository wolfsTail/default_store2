from enum import unique
from django.db import models


class Categories(models.Model):
    name = models.CharField(
        max_length=128, unique=True, verbose_name="Наименование категории"
    )
    slug = models.SlugField(
        max_length=192, unique=True, blank=True, null=True, verbose_name="URL"
    )

    class Meta:
        db_table = "category"
        verbose_name = "Категорию"
        verbose_name_plural = "Категории"

    def __str__(self):
        return f"{self.name}"


class Products(models.Model):
    name = models.CharField(
        max_length=128, unique=True, verbose_name="Наименование продукта"
    )
    slug = models.SlugField(
        max_length=192, unique=True, blank=True, null=True, verbose_name="URL"
    )
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    image = models.ImageField(
        upload_to="goods_images", blank=True, null=True, verbose_name="Изображение"
    )
    price = models.DecimalField(
        default=0.00,
        max_digits=8,
        decimal_places=2,
        verbose_name="Стоимость за единицу",
    )
    discount = models.DecimalField(
        default=0.00,
        max_digits=4,
        decimal_places=2,
        verbose_name="скидка за единицу в процентах",
    )
    quantity = models.PositiveIntegerField(default=0, verbose_name="Количетсво")
    category = models.ForeignKey(
        Categories, on_delete=models.CASCADE, verbose_name="Связанная категория"
    )

    class Meta:
        db_table = "product"
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
    
    def __str__(self):
        return f"{self.name}, кол-во - {self.quantity}"
