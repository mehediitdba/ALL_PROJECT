# Generated by Django 4.0.5 on 2022-06-26 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mPOSApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='t_registration',
            name='reg_id',
            field=models.IntegerField(default=1),
        ),
    ]
