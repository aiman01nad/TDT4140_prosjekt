# Generated by Django 4.1.7 on 2023-03-21 13:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0017_merge_20230321_1427'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='isReported',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('GENERELL', 'Generell'), ('BIL', 'Bil'), ('BYGG', 'Bygg'), ('BÅT', 'Båt'), ('FRITID', 'Fritid'), ('HAGEARBEID', 'Hagearbeid'), ('HJEMME', 'Hjemme'), ('KJØKKEN', 'Kjøkken'), ('SPORT', 'Sport')], default='Generell', max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 21, 14, 59, 28, 158820), verbose_name='date published'),
        ),
        migrations.DeleteModel(
            name='Rental',
        ),
    ]