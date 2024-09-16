from django.db import models

from shop.validators import ShopValidator


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    model = models.CharField(max_length=255, verbose_name="Модель")
    release_date = models.DateField(verbose_name="Дата выхода продукта на рынок")

    def __str__(self):
        return f"{self.name} ({self.model})"


class ShopNode(models.Model):
    NODE_TYPES = (
        (0, 'Завод'),
        (1, 'Розничная сеть'),
        (2, 'Индивидуальный предприниматель'),
    )

    name = models.CharField(max_length=255, verbose_name='Наименование')
    email = models.EmailField(verbose_name='Email')
    country = models.CharField(max_length=100, verbose_name='Страна')
    city = models.CharField(max_length=100, verbose_name='Город')
    street = models.CharField(max_length=100, verbose_name='Улица')
    house_number = models.CharField(max_length=10, verbose_name='Номер дома')
    debt = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Задолженность',
                               help_text='числа через точку в дроби', default=0)
    products = models.ManyToManyField(Product, related_name='nodes')
    supplier = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='Поставщик', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    node_type = models.IntegerField(choices=NODE_TYPES, verbose_name='Тип узла')

    def __str__(self):
        return self.name

    def clean(self):
        validator = ShopValidator('node_type', 'supplier', 'pk')
        validator(self)
        super().clean()
