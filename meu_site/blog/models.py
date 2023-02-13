from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

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

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.slug])

    def get_absolute_url_2(self):
        return reverse('post_edit', args=[self.pk])

    def get_absolute_url_3(self):
        return reverse('post_delete', args=[self.pk])

    class Meta:
        ordering = ('posted',)

    def __str__(self):
        return self.title


# Create your models here.