# Generated by Django 4.0.5 on 2022-07-02 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('pid', models.BigIntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=60)),
                ('description', models.TextField(max_length=1000)),
                ('price', models.FloatField()),
                ('weight', models.FloatField()),
                ('category', models.CharField(max_length=20)),
                ('delivery', models.SmallIntegerField(default=7)),
                ('stock', models.BooleanField(default=True)),
                ('image', models.ImageField(upload_to='upload')),
            ],
        ),
    ]
