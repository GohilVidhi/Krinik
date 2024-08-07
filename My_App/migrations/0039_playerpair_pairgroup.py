# Generated by Django 5.0.6 on 2024-07-17 04:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('My_App', '0038_login_user_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerPair',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('limit', models.IntegerField()),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='My_App.match')),
                ('player_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player_1', to='My_App.player')),
                ('player_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player_2', to='My_App.player')),
                ('pool', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='My_App.add_pool')),
            ],
        ),
        migrations.CreateModel(
            name='PairGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='My_App.match')),
                ('pool', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='My_App.add_pool')),
                ('pairs', models.ManyToManyField(to='My_App.playerpair')),
            ],
        ),
    ]
