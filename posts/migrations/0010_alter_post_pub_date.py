# Generated by Django 3.2.12 on 2023-02-16 21:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_auto_20230216_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 16, 22, 34, 15, 819336), verbose_name='date published'),
        ),
    ]