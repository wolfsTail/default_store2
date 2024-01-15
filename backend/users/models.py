from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True, verbose_name="Электронная почта")
    image = models.ImageField(upload_to="users_images", blank=True, null=True, verbose_name="Аватар")
    phone_number = models.CharField(max_length=14, blank=True, null=True, verbose_name="Номер телефона")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']

    class Meta:
        db_table = 'user'
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Пользователи'
