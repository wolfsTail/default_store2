from django.contrib import admin

from .models import Categories, Products


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}
    ordering = ("name",)


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ("name", "quantity", "price", "discount")
    list_editable = ("discount", "quantity")
    search_fields = ("name", "description", "category__name")
    list_filter = ("category", "discount", "quantity")
    fields = (
        "name",
        "category",        
        "description",
        ("quantity", "price", "discount"),
        "image",
        "slug",        
    )
