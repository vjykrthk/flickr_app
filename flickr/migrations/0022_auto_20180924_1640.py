# Generated by Django 2.1.1 on 2018-09-24 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flickr', '0021_flickrphotonote'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flickrphoto',
            name='notes',
        ),
        migrations.AddField(
            model_name='flickrphotonote',
            name='flickr_photo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='flickr.FlickrPhoto'),
            preserve_default=False,
        ),
    ]
