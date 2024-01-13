from django.db import models


class IndexPageContent(models.Model):
    title = models.CharField(
        max_length=128, verbose_name="Заголовок на странице", default="Default title"
    )
    content = models.TextField(
        verbose_name="Контент на главной странице",
        default="Default shop empty content!",
    )
    created_timestamp = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата и время описания"
    )

    class Meta:
        db_table = "index_page_content"
        verbose_name = "Контент на главной странице"
        verbose_name_plural = "Контент на главной странице"


class AboutPageContent(models.Model):
    title = models.CharField(
        max_length=128, verbose_name="Заголовок на странице", default="Default title"
    )
    content = models.TextField(
        verbose_name="Контент на странице 'О нас'",
        default="Default shop empty content 'about page'!",
    )
    text_in_page = models.TextField(
        verbose_name="Текст на странице", default="Text on about page"
    )
    created_timestamp = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата и время описания"
    )

    class Meta:
        db_table = "about_page_content"
        verbose_name = "Контент на странице 'О нас'"
        verbose_name_plural = "Контент на странице 'О нас'"


class PayAndDeliveryPageContent(models.Model):
    title = models.CharField(
        max_length=128, verbose_name="Заголовок на странице", default="Default title"
    )
    content = models.TextField(
        verbose_name="Контент на странице 'Оплата и доставка'",
        default="Default shop empty content 'pay and delivery'!",
    )
    text_in_page = models.TextField(
        verbose_name="Текст на странице", default="Text on 'pay and delivery' page"
    )
    created_timestamp = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата и время описания"
    )

    class Meta:
        db_table = "pay_and_delivery_page_content"
        verbose_name = "Контент на странице 'Оплата и доставка'"
        verbose_name_plural = "Контент на странице 'Оплата и доставка'"


class InformationPageContent(models.Model):
    title = models.CharField(
        max_length=128, verbose_name="Заголовок на странице", default="Default title"
    )
    content = models.TextField(
        verbose_name="Контент на странице 'Контактная информация'",
        default="Default shop empty content 'information'!",
    )
    text_in_page = models.TextField(
        verbose_name="Текст на странице", default="Text on 'pay and delivery' page"
    )
    created_timestamp = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата и время описания"
    )

    class Meta:
        db_table = "information_page_content"
        verbose_name = "Контент на странице 'Контактная информация'"
        verbose_name_plural = "Контент на странице 'Контактная информация'"
