from django.db import models
from autoslug import AutoSlugField

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='products')
    cover_image = models.ImageField(upload_to='cover_image', null=True, blank=True)
    price = models.FloatField()
    currency =  models.CharField(max_length=20, default="usd")
    info = models.CharField(max_length=255, null=True, blank=True)
    short_description = models.TextField(max_length=200, null=True, blank=True)
    full_description = models.TextField(max_length=500, null=True, blank=True)
    slug = AutoSlugField(populate_from='name')
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name