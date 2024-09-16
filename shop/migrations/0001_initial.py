# Generated by Django 4.2 on 2024-09-16 19:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="Название")),
                ("model", models.CharField(max_length=255, verbose_name="Модель")),
                (
                    "release_date",
                    models.DateField(verbose_name="Дата выхода продукта на рынок"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ShopNode",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="Наименование")),
                ("email", models.EmailField(max_length=254, verbose_name="Email")),
                ("country", models.CharField(max_length=100, verbose_name="Страна")),
                ("city", models.CharField(max_length=100, verbose_name="Город")),
                ("street", models.CharField(max_length=100, verbose_name="Улица")),
                (
                    "house_number",
                    models.CharField(max_length=10, verbose_name="Номер дома"),
                ),
                (
                    "debt",
                    models.DecimalField(
                        decimal_places=2,
                        default=0,
                        help_text="числа через точку в дроби",
                        max_digits=10,
                        verbose_name="Задолженность",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата создания"
                    ),
                ),
                (
                    "node_type",
                    models.IntegerField(
                        choices=[
                            (0, "Завод"),
                            (1, "Розничная сеть"),
                            (2, "Индивидуальный предприниматель"),
                        ],
                        verbose_name="Тип узла",
                    ),
                ),
                (
                    "products",
                    models.ManyToManyField(related_name="nodes", to="shop.product"),
                ),
                (
                    "supplier",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="shop.shopnode",
                        verbose_name="Поставщик",
                    ),
                ),
            ],
        ),
    ]
