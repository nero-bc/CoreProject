# Generated by Django 4.1.7 on 2023-03-09 03:14

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="token",
            unique_together={("token", "user")},
        ),
    ]
