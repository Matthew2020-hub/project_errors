from django.db import models
import uuid

# Create your models here.
class Apartment(models.Model):
    
    apartment_id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, unique=True)
    name = models.CharField(max_length=40, null=True)
    category = models.CharField(max_length=50, null=True)
    # image = models.ImageField()
    price = models.CharField(max_length=50, null=True)
    location = models.CharField(max_length=30, null=True)
    agent = models.CharField(max_length=30, null=True)

    class Meta:
        ordering = ['category']