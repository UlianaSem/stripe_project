from django.contrib import admin

from main.models import Item, Discount, Tax, ItemOrder, Order

admin.site.register(Item)

admin.site.register(Discount)

admin.site.register(Tax)

admin.site.register(ItemOrder)

admin.site.register(Order)
