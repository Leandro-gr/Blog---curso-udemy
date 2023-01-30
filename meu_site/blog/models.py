from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    STATS =  (
        ('rascunho', 'Rascunho'),
        ('publicado', 'Publicado')
    )

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    contents = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    posted = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    changed = models.DateTimeField(auto_now=True)
    stats = models.CharField(max_length=10, choices=STATS, default='rascunho')

    class Meta:
        ordering = ('posted',)

    def __str__(self):
        return self.title


# Create your models here.