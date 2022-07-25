# Generated by Django 4.0.5 on 2022-07-16 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Out for delivery', 'Out for delivery'), ('Delivered', 'Delivered'), ('Canceled', 'Canceled')], max_length=30),
        ),
    ]