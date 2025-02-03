# Generated by Django 4.2.18 on 2025-02-03 15:53

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_collaborationrequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='consultingassignment',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
    ]
