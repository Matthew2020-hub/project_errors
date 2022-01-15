from rest_framework import serializers
from .models import Apartment
from django.db.models.base import ModelState
from django.db import models

class ApartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apartment
        fields = ['apartment_id', 'name','category', 'price', 'location', 'agent']