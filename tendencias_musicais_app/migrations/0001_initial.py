# Generated by Django 3.0.8 on 2020-07-23 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Playlists',
            fields=[
                ('playlist_id', models.CharField(max_length=126, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=126)),
                ('country', models.CharField(max_length=126)),
                ('source', models.CharField(max_length=126)),
            ],
        ),
    ]
