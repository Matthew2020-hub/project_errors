from django.db import models

# Create your models here.
class Apartment(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=40, null=True)
    category = models.CharField(max_length=50, null=True)
    # image = models.ImageField()
    price = models.CharField(max_length=50, null=True)
    location = models.CharField(max_length=30, null=True)
    agent = models.CharField(max_length=30, null=True)

    class Meta:
        ordering = ['category']