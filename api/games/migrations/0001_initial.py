# Generated by Django 3.1.14 on 2022-02-02 14:50

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('release_date', models.DateField(default=datetime.date.today)),
                ('platforms', models.JSONField(blank=True, null=True)),
                ('requirements', models.JSONField(blank=True, null=True)),
                ('genres', models.JSONField(blank=True, null=True)),
                ('tags', models.JSONField(blank=True, null=True)),
                ('metacritic_rating', models.CharField(default='Not set', max_length=8)),
                ('esb_rating', models.CharField(default='None', max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='UserGameRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.BooleanField(default=False)),
                ('in_bookmarks', models.BooleanField(default=False)),
                ('rate', models.PositiveSmallIntegerField(choices=[(1, 'Bad'), (2, 'Not good'), (3, 'Ok'), (4, 'Good'), (5, 'Super')], null=True)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.game')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='subscribers',
            field=models.ManyToManyField(related_name='games', through='games.UserGameRelation', to=settings.AUTH_USER_MODEL),
        ),
    ]