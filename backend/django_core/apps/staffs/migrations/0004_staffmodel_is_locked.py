# Generated by Django 4.2 on 2023-04-24 07:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("staffs", "0003_staffmodel_created_at_staffmodel_updated_at"),
    ]

    operations = [
        migrations.AddField(
            model_name="staffmodel",
            name="is_locked",
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
