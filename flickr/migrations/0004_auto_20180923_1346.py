# Generated by Django 2.1.1 on 2018-09-23 13:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('flickr', '0003_auto_20180923_1221'),
    ]

    operations = [
        migrations.CreateModel(
            name='FlickrPhotoLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.DecimalField(decimal_places=30, max_digits=50)),
                ('longitude', models.DecimalField(decimal_places=30, max_digits=50)),
                ('accuracy', models.IntegerField()),
                ('context', models.IntegerField()),
                ('place_id', models.CharField(max_length=200)),
                ('woeid', models.CharField(max_length=200)),
            ],
        ),
        migrations.RenameModel(
            old_name='FlickrPhotoDates',
            new_name='FlickrPhotoDate',
        ),
        migrations.RenameModel(
            old_name='FlickrPhotos',
            new_name='FlickrPhoto',
        ),
        migrations.AddField(
            model_name='flickrphotolocation',
            name='flickr_photo',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='flickr.FlickrPhoto'),
        ),
    ]
