# Generated by Django 4.1.6 on 2023-02-14 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_rename_admin_user_is_admin_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_admin',
            new_name='admin',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='is_staff',
            new_name='staff',
        ),
    ]
