from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.db.models.deletion import CASCADE, PROTECT
from django.db.models.fields import TextField
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify


class Category(models.Model):
    GETTING_STARTED = "GS"
    DIY = "DIY"
    GARDENS = "GR"
    TERRARIUMS = "TR"
    CATEGORY_TYPE = [
        (GETTING_STARTED, "Getting Started"),
        (DIY, "DIY"),
        (GARDENS, "Gardens"),
        (TERRARIUMS, "Terrariums"),
    ]
    name = models.CharField(max_length=100)
    kind = models.CharField(max_length=3, choices=CATEGORY_TYPE, default=" ")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    slug = models.SlugField(unique=True, default="", blank=True)
    image = models.ImageField(upload_to="images/")
    content = RichTextUploadingField(config_name="default", blank=True, null=True)
    summary = models.CharField(max_length=150, unique=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("core:post_detail", args=[str(self.slug)])

    class Meta:
        ordering = ["-created_date"]


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments", null=True)
    name = models.CharField(max_length=80, null=True)
    email = models.EmailField(null=True)
    body = models.TextField(null=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    active = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['created_on']
    
    def __str__(self):
        return f'Comment {self.body} by {self.name}'



class Picture(models.Model):
    title = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to="images/gallery/")
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        ordering = ["-created_date"]

