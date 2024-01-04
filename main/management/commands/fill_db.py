from django.core.management import BaseCommand

from main.models import Item, Tax, Discount, Order, ItemOrder


class Command(BaseCommand):

    items = [
        {"name": "item_1", "description":  "item_1", "price": 10000.0, "currency": "rub"},
        {"name": "item_2", "description":  "item_2", "price": 15000.0, "currency": "rub"},
        {"name": "item_3", "description":  "item_3", "price": 10000.0, "currency": "usd"},
    ]

    def handle(self, *args, **options):

        item_1 = Item.objects.create(**self.items[0])
        item_2 = Item.objects.create(**self.items[1])
        item_3 = Item.objects.create(**self.items[2])

        tax = Tax.objects.create(value=13)
        discount = Discount.objects.create(value=25)

        order_1 = Order.objects.create()
        order_2 = Order.objects.create(tax=tax, discount=discount)

        ItemOrder.objects.create(item=item_1, order=order_1, quantity=3)
        ItemOrder.objects.create(item=item_2, order=order_1, quantity=2)

        ItemOrder.objects.create(item=item_3, order=order_2, quantity=2)
