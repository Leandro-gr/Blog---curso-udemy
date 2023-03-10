from django.db import models
from django.dispatch import receiver
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from django.db.models.signals import post_save
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=100)
    posted = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "categoria"

    def __str__(self):
        return self.name

class Post(models.Model):
    STATS =  (
        ('rascunho', 'Rascunho'),
        ('publicado', 'Publicado')
    )

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    contents = RichTextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, related_name='get_posts')
    image = models.ImageField(upload_to="blog",blank=True, null=True)
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

@receiver(post_save,sender=Post)
def insert_slug(sender,instance,**kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)
        return instance.save()

# Create your models here.