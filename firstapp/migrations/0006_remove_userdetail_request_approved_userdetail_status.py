# Generated by Django 5.0.2 on 2024-03-11 11:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("firstapp", "0005_userdetail_request_approved"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="userdetail",
            name="request_approved",
        ),
        migrations.AddField(
            model_name="userdetail",
            name="status",
            field=models.CharField(default=None, max_length=50),
        ),
    ]