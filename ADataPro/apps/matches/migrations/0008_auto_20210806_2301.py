# Generated by Django 3.2.4 on 2021-08-06 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0007_alter_teamsinfo_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='matches',
            name='img_link_team1',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='matches',
            name='img_link_team2',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teamsinfo',
            name='img_link_team',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]
