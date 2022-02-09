# Generated by Django 3.1.14 on 2022-02-09 00:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0016_auto_20220209_0010'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='comments',
            field=models.ManyToManyField(related_name='comments', through='articles.Comment', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='article',
            name='readers',
            field=models.ManyToManyField(related_name='articles', through='articles.UserArticleRelation', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.article'),
        ),
    ]
