# Generated by Django 3.2.16 on 2022-10-28 12:00

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_category_filter',
            field=models.CharField(choices=[('gaps', 'Gaps'), ('rails', 'Rail'), ('ledges', 'Ledges'), ('street', 'Street')], default='gaps', max_length=50),
        ),
        migrations.AlterField(
            model_name='post',
            name='video',
            field=cloudinary.models.CloudinaryField(default='../default_VID', max_length=255),
        ),
    ]
