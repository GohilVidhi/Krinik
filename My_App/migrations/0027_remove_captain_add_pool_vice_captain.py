# Generated by Django 5.0.6 on 2024-07-02 06:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('My_App', '0026_captain_add_pool_vice_captain'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='captain_add_pool',
            name='vice_captain',
        ),
    ]
