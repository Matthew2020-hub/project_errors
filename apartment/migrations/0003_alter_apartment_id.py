# Generated by Django 4.0.1 on 2022-01-13 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartment', '0002_remove_apartment_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]
