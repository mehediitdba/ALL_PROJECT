# Generated by Django 4.0.5 on 2022-07-16 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cartapp', '0002_cartitem_price_cartitem_qty'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='ordered',
            field=models.BooleanField(default=False),
        ),
    ]
