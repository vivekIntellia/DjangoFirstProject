# Generated by Django 5.0.2 on 2024-03-11 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='phoneotp',
            managers=[
            ],
        ),
        migrations.AlterUniqueTogether(
            name='phoneotp',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='phoneotp',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='phoneotp',
            name='email',
        ),
        migrations.RemoveField(
            model_name='phoneotp',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='phoneotp',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='phoneotp',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='phoneotp',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='phoneotp',
            name='username',
        ),
    ]
