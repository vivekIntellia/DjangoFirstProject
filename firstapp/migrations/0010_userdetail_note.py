# Generated by Django 5.0.2 on 2024-03-13 12:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("firstapp", "0009_alter_userdetail_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="userdetail",
            name="note",
            field=models.CharField(default="", max_length=100),
        ),
    ]