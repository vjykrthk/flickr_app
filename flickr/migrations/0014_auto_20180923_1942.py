# Generated by Django 2.1.1 on 2018-09-23 19:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flickr', '0013_auto_20180923_1938'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flickrphotourl',
            old_name='type',
            new_name='url_type',
        ),
    ]
