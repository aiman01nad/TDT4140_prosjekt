# Generated by Django 4.1.6 on 2023-02-14 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_rename_is_admin_user_admin_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
