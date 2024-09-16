from django.contrib import admin

from .models import Product, ShopNode


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "model", "release_date")
    search_fields = ("name", "model")


@admin.register(ShopNode)
class ShopNodeAdmin(admin.ModelAdmin):
    list_display = ("name", "node_type", "city", "supplier", "debt", "created_at")
    list_filter = ("city",)
    search_fields = ("name",)
    filter_horizontal = ("products",)

    actions = ["clear_debt"]

    def clear_debt(self, request, queryset):
        queryset.update(debt=0)

    clear_debt.short_description = "Очистить задолженность перед поставщиком"
