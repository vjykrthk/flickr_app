# Generated by Django 2.1.1 on 2018-09-24 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flickr', '0018_flickrgroup_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flickrphoto',
            name='flickr_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flickr_photos', to='flickr.FlickrGroup'),
        ),
    ]
