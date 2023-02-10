# Generated by Django 4.1.6 on 2023-02-09 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0004_post_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="image_url",
            field=models.ImageField(blank=True, upload_to="productImages/"),
        ),
        migrations.AlterField(
            model_name="post",
            name="status",
            field=models.CharField(
                choices=[(1, "available"), (0, "unavailable")],
                default=1,
                max_length=200,
            ),
        ),
    ]
