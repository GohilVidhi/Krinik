# Generated by Django 5.0.6 on 2024-06-28 10:18

import django.db.models.deletion
import django_mysql.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('My_App', '0016_delete_demo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Add_Pool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pool_type', models.CharField(blank=True, max_length=50, null=True)),
                ('pool_name', models.CharField(blank=True, max_length=50, null=True)),
                ('price', django_mysql.models.ListTextField(models.IntegerField(), blank=True, null=True, size=100)),
                ('winning_price', models.IntegerField()),
                ('fantacy_start_date', models.CharField(blank=True, max_length=50, null=True)),
                ('fantacy_end_date', models.CharField(blank=True, max_length=50, null=True)),
                ('select_match', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='My_App.match')),
            ],
        ),
    ]
