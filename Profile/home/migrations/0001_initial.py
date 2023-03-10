# Generated by Django 4.1.5 on 2023-01-17 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="message",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.TextField(
                        blank=True,
                        help_text="enter your name",
                        max_length=50,
                        null=True,
                    ),
                ),
                (
                    "text",
                    models.TextField(
                        help_text="enter your message , ending with your details,contact number and phone number",
                        max_length=1000,
                    ),
                ),
            ],
        ),
    ]
