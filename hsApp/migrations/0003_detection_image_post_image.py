# Generated by Django 4.2.7 on 2024-02-28 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hsApp', '0002_detection_url_post_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='detection',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
