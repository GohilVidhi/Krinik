# Generated by Django 5.0.6 on 2024-07-17 06:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('My_App', '0039_playerpair_pairgroup'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playerpair',
            name='match',
        ),
        migrations.RemoveField(
            model_name='playerpair',
            name='player_1',
        ),
        migrations.RemoveField(
            model_name='playerpair',
            name='player_2',
        ),
        migrations.RemoveField(
            model_name='playerpair',
            name='pool',
        ),
        migrations.DeleteModel(
            name='PairGroup',
        ),
        migrations.DeleteModel(
            name='PlayerPair',
        ),
    ]