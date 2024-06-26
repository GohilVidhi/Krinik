# Generated by Django 5.0.4 on 2024-06-19 09:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('My_App', '0002_alter_league_end_league_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(blank=True, max_length=50, null=True)),
                ('team_short_name', models.CharField(blank=True, max_length=50, null=True)),
                ('team_image', models.ImageField(upload_to='league_image_media')),
                ('team_date', models.DateField(auto_now=True)),
                ('league_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='My_App.league')),
            ],
        ),
    ]
