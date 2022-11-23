
from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Group(models.Model):
    """Модель групп"""
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True,)
    description = models.TextField()

    def __str__(self):
        return self.title


class Post(models.Model):
    '''Модель постов'''
    class Meta:
        ordering = ['-pub_date']
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    group = models.ForeignKey(
        Group,
        related_name='Group',
        on_delete=models.SET_NULL,
        blank=True, null=True,
    )

    def __str__(self):
        return self.text
