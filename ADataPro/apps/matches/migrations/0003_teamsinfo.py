# Generated by Django 3.2.4 on 2021-08-03 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0002_auto_20210803_0230'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamsInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matchID', models.IntegerField()),
                ('team_name', models.CharField(max_length=200)),
                ('wins', models.IntegerField()),
                ('losses', models.IntegerField()),
                ('draws', models.IntegerField()),
                ('points', models.IntegerField()),
            ],
        ),
    ]
