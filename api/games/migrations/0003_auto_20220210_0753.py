# Generated by Django 3.1.14 on 2022-02-10 07:53

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('games', '0002_auto_20220209_0051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='subscribers',
            field=models.ManyToManyField(related_name='games', through='games.UserGameRelation', to=settings.AUTH_USER_MODEL),
        ),
    ]
