# Generated by Django 4.0.6 on 2022-09-14 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('per_code', models.CharField(max_length=3)),
                ('mobile', models.CharField(max_length=15)),
            ],
        ),
    ]