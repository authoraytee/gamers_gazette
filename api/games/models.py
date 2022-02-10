from django.db import models
from accounts.models import CustomUser
import datetime

class Game(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    release_date = models.DateField(default=datetime.date.today)
    platforms = models.JSONField(blank=True, null=True)
    requirements = models.JSONField(blank=True, null=True)
    genres = models.JSONField(blank=True, null=True)
    tags = models.JSONField(blank=True, null=True)
    metacritic_rating = models.CharField(max_length=8, default='Not set')
    esb_rating = models.CharField(max_length=25, default='None')
    cover = models.ImageField(blank=True, upload_to='games/covers/')

    subscribers = models.ManyToManyField(CustomUser, through='UserGameRelation', related_name='games')

    def __str__(self):
        return f'Id {self.id}: {self.name}'

class UserGameRelation(models.Model):
    RATE_CHOICES = (
        (1, 'Bad'),
        (2, 'Not good'),
        (3, 'Ok'),
        (4, 'Good'),
        (5, 'Super'),
    )

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    like = models.BooleanField(default=False)
    in_bookmarks = models.BooleanField(default=False) 
    rate = models.PositiveSmallIntegerField(choices=RATE_CHOICES, null=True)

    def __str__(self):
        return f'{self.user.username} - game:{self.game.id}.{self.game.name}, rate:{self.rate}'
