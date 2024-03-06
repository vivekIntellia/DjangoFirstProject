# Generated by Django 5.0.2 on 2024-02-29 09:05

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="firstapp",
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
                ("firstapp_icon", models.CharField(max_length=50)),
                ("firstapp_title", models.CharField(max_length=50)),
                ("firstapp_des", models.TextField()),
            ],
        ),
    ]
