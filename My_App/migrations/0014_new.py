# Generated by Django 5.0.4 on 2024-06-26 05:24

import django_mysql.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('My_App', '0013_pool_league_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='new',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('widget_group_ids', django_mysql.models.ListTextField(models.IntegerField(), blank=True, null=True, size=100)),
            ],
        ),
    ]
