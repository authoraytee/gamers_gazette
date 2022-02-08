from django.db import models
from accounts.models import CustomUser
from django.contrib.auth import get_user_model

class Article(models.Model):
    title = models.CharField(max_length=150)
    link = models.CharField(max_length=175)
    text = models.TextField()
    site = models.CharField(max_length=25, default='gamers gazetter')
    pub_date = models.DateTimeField(auto_now_add=True)
    cover = models.ImageField(blank=True, upload_to='articles/covers/')

    owner = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name='my_articles')
    readers = models.ManyToManyField(CustomUser, through='UserArticleRelation', related_name='articles')

    def __str__(self):
        return f'Id {self.id}: {self.title}'


class UserArticleRelation(models.Model):
    RATE_CHOICES = (
        (1, 'Bad'),
        (2, 'Not good'),
        (3, 'Ok'),
        (4, 'Good'),
        (5, 'Super'),
    )

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    like = models.BooleanField(default=False)
    in_bookmarks = models.BooleanField(default=False) 
    rate = models.PositiveSmallIntegerField(choices=RATE_CHOICES, null=True)

    def __str__(self):
        return f'{self.user.username} - article:{self.article.id}.{self.article.title}, rate:{self.rate}'

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.comment