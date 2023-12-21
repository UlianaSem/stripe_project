from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=255, verbose_name='название')
    description = models.TextField(verbose_name='описание', null=True, blank=True)
    price = models.FloatField(verbose_name='цена')

    def __str__(self):
        return f'{self.name}, цена {self.price}'

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
