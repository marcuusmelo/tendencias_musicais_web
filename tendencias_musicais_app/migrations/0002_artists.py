# Generated by Django 3.0.8 on 2020-07-23 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tendencias_musicais_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artists',
            fields=[
                ('artist_id', models.CharField(max_length=126, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=126)),
                ('music_genre_1', models.CharField(max_length=126)),
                ('music_genre_2', models.CharField(max_length=126)),
                ('music_genre_3', models.CharField(max_length=126)),
            ],
        ),
    ]
