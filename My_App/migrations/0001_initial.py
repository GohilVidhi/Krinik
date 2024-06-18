# Generated by Django 5.0 on 2024-06-18 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('league_name', models.CharField(blank=True, max_length=50, null=True)),
                ('short_league_name', models.CharField(blank=True, max_length=50, null=True)),
                ('start_league_date', models.DateTimeField()),
                ('end_league_date', models.DateTimeField()),
                ('league_image', models.ImageField(upload_to='league_image_media')),
            ],
        ),
    ]
