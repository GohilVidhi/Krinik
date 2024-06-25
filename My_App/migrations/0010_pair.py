# Generated by Django 5.0.4 on 2024-06-24 06:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('My_App', '0009_rename_end_league_date_pool_end_pool_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pair',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('limit', models.IntegerField()),
                ('player_1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pool_player1', to='My_App.player')),
                ('player_2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pool_player2', to='My_App.player')),
                ('pool_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='My_App.pool')),
            ],
        ),
    ]
