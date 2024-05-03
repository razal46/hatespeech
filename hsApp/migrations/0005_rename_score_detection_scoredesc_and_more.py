# Generated by Django 4.2.7 on 2024-04-08 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hsApp', '0004_tags_remove_detection_image_remove_detection_url_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detection',
            old_name='score',
            new_name='scoreDesc',
        ),
        migrations.AddField(
            model_name='detection',
            name='scoreTitle',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='tags',
            name='neCount',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='tags',
            name='nuCount',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='tags',
            name='poCount',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='tags',
            name='totalCount',
            field=models.IntegerField(null=True),
        ),
    ]
