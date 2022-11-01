# Generated by Django 3.2.16 on 2022-11-01 10:50

import cloudinary_storage.storage
import cloudinary_storage.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postvideo', '0007_videopost_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videopost',
            name='video',
            field=models.ImageField(blank=True, storage=cloudinary_storage.storage.VideoMediaCloudinaryStorage(), upload_to='videos/', validators=[cloudinary_storage.validators.validate_video]),
        ),
    ]
