# Generated by Django 4.2.11 on 2024-04-29 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todos", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("name", models.CharField(max_length=50)),
                ("email", models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name="Todo",
        ),
    ]