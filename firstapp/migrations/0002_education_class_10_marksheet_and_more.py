# Generated by Django 5.0.2 on 2024-03-19 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='class_10_marksheet',
            field=models.ImageField(blank=True, null=True, upload_to='marksheet/'),
        ),
        migrations.AddField(
            model_name='education',
            name='class_10_percentage',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='education',
            name='class_12_marksheet',
            field=models.ImageField(blank=True, null=True, upload_to='marksheet/'),
        ),
        migrations.AddField(
            model_name='education',
            name='class_12_percentage',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='education',
            name='graduation_marksheet',
            field=models.ImageField(blank=True, null=True, upload_to='marksheet/'),
        ),
        migrations.AddField(
            model_name='education',
            name='graduation_percentage',
            field=models.FloatField(blank=True, null=True),
        ),
    ]