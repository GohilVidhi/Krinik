# Generated by Django 5.0.6 on 2024-07-15 09:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('My_App', '0032_pair_with_captain'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pair_with_captain_v_captain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('limit', models.IntegerField()),
                ('player_1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pair_with_v1', to='My_App.player')),
                ('player_2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pair_with_v2', to='My_App.player')),
                ('pool_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='My_App.add_pool')),
            ],
        ),
    ]
