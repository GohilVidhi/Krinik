# Generated by Django 5.0.6 on 2024-06-28 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('My_App', '0018_rename_select_team_2_match_select_team_b'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='match_display_name',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]