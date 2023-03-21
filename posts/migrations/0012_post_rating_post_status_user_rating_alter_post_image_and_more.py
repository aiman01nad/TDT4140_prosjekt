# Generated by Django 4.1.6 on 2023-03-07 13:09

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_auto_20230221_1739'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='rating',
            field=models.IntegerField(default=5, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('AVAILABLE', 'available'), ('UNAVAILABLE', 'unavailable')], default='AVAILABLE', max_length=200),
        ),
        migrations.AddField(
            model_name='user',
            name='rating',
            field=models.IntegerField(default=5, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 7, 14, 9, 16, 329877), verbose_name='date published'),
        ),
    ]
