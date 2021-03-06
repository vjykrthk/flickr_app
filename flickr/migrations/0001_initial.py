# Generated by Django 2.1.1 on 2018-09-23 07:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FlickrGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flckr_id', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='FlickrPhotos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flickr_id', models.CharField(max_length=200)),
                ('secret', models.CharField(max_length=200)),
                ('server', models.CharField(max_length=100)),
                ('farm', models.IntegerField()),
                ('dateuploaded', models.DateTimeField()),
                ('isfavorite', models.BooleanField()),
                ('license', models.BooleanField()),
                ('safety_level', models.IntegerField()),
                ('rotation', models.IntegerField()),
                ('originalformat', models.CharField(max_length=50)),
                ('views', models.IntegerField()),
                ('media', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='FlickrPhotoUrl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('flickr_photo_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='urls', to='flickr.FlickrPhotos')),
            ],
        ),
    ]
