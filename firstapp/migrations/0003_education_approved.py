# Generated by Django 5.0.2 on 2024-03-20 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_education_class_10_marksheet_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]