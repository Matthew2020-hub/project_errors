# Generated by Django 4.0.1 on 2022-01-15 21:18

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('apartment_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=40, null=True)),
                ('category', models.CharField(max_length=50, null=True)),
                ('price', models.CharField(max_length=50, null=True)),
                ('location', models.CharField(max_length=30, null=True)),
                ('agent', models.CharField(max_length=30, null=True)),
            ],
            options={
                'ordering': ['category'],
            },
        ),
    ]
