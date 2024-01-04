from django.db import models
from django.db.models import TextChoices

from main.utils import get_exchange_rate


class CurrencyChoice(TextChoices):
    rub = "rub"
    usd = "usd"


class Item(models.Model):
    name = models.CharField(max_length=255, verbose_name='название')
    description = models.TextField(verbose_name='описание', null=True, blank=True)
    price = models.FloatField(verbose_name='цена')
    currency = models.CharField(max_length=3, choices=CurrencyChoice)

    def __str__(self):
        return f'{self.name}, цена {self.price}'

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'


class Discount(models.Model):
    """Модель Discount, которую можно прикрепить к модели Order"""
    value = models.FloatField(verbose_name='размер скидки')

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = 'скидка'
        verbose_name_plural = 'скидки'


class Tax(models.Model):
    """Модель Tax, которую можно прикрепить к модели Order"""
    value = models.FloatField(verbose_name='размер налога')

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = 'налог'
        verbose_name_plural = 'налоги'


class ItemOrder(models.Model):
    """Модель ItemOrder, которая связывает Item и Order"""
    item = models.ForeignKey(Item, verbose_name="товар", on_delete=models.CASCADE)
    order = models.ForeignKey("Order", verbose_name="заказ", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name="количество")

    def __str__(self):
        return f"{self.order}: {self.item}, {self.quantity}"

    @property
    def full_price(self):
        """Высчитывает полную стоимость продукта в заказе"""
        if self.item.currency == "usd":
            rate = get_exchange_rate(self.item.currency)
            price = round(self.item.price / rate, 2)

        else:
            price = self.item.price

        return round(price * self.quantity, 2)


class Order(models.Model):
    """Модель Order, в которой можно объединить несколько Items"""
    items = models.ManyToManyField(
        Item, through='ItemOrder', through_fields=('order', 'item')
    )

    tax = models.ForeignKey(Tax, verbose_name="налог", null=True, blank=True, on_delete=models.SET_NULL)
    discount = models.ForeignKey(Discount, verbose_name="скидка", null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.pk}"

    @property
    def order_full_price(self):
        """Высчитывает полную стоимость заказа"""
        items = self.items.through.objects.filter(order=self)
        prices = [
            round(item.full_price, 2) for item in items
        ]
        return round(sum(prices), 2)

    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'
