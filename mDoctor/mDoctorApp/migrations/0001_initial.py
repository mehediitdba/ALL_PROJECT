# Generated by Django 4.0.6 on 2022-07-19 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='t_Appiontment',
            fields=[
                ('appid', models.BigIntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('app_name', models.CharField(max_length=60)),
                ('app_email', models.EmailField(max_length=50)),
                ('app_phone', models.CharField(max_length=20)),
                ('app_date', models.DateField()),
                ('app_dept', models.CharField(max_length=20)),
                ('app_doc', models.CharField(max_length=20)),
                ('app_comments', models.CharField(max_length=200)),
            ],
        ),
    ]