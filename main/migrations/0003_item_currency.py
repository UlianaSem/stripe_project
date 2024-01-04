# Generated by Django 5.0 on 2024-01-04 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_discount_tax_itemorder_order_itemorder_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='currency',
            field=models.CharField(choices=[('rub', 'Rub'), ('usd', 'Usd')], default='rub', max_length=3),
            preserve_default=False,
        ),
    ]
