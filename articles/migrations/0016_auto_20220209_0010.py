# Generated by Django 3.1.14 on 2022-02-09 00:10

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0015_auto_20220209_0000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='readers',
            field=models.ManyToManyField(related_name='articles', through='articles.UserArticleRelation', to=settings.AUTH_USER_MODEL),
        ),
    ]
