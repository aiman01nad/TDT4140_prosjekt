# Generated by Django 4.1.7 on 2023-03-21 14:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0019_alter_post_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 21, 15, 0, 33, 818709), verbose_name='date published'),
        ),
    ]