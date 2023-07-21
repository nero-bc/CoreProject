# Generated by Django 4.2.3 on 2023-07-21 13:13

import apps.user.validators.username
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0006_customuser_created_at"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="customuser",
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="username",
            field=models.CharField(
                error_messages={"unique": "A user with that username already exists."},
                help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                max_length=150,
                unique=True,
                validators=[
                    apps.user.validators.username.username_validator,
                    django.core.validators.RegexValidator(
                        "^[a-zA-Z0-9_-]+#[0-9]{4}$",
                        message="Username is not valid for this regex `^[a-zA-Z0-9_-]+#[0-9]{4}$`",
                    ),
                ],
                verbose_name="username",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="customuser",
            unique_together={("username", "email")},
        ),
        migrations.RemoveField(
            model_name="customuser",
            name="discriminator",
        ),
    ]
