from django.db import models
from django.db.models.deletion import CASCADE, PROTECT
from django.db.models.fields import TextField
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField


class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name



class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    slug = models.SlugField(unique=True, default='', blank=True)
    image = models.ImageField(upload_to='images/')
    content = TextField(null=True, blank=True)
    summary = models.CharField(max_length=150, unique=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('core:post_detail', args=[str(self.slug)])

    class Meta:
        ordering = ['-created_date']


class Picture(models.Model):
    title = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='images/gallery/')
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ['-created_date']