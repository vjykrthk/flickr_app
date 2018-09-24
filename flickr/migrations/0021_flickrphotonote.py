# Generated by Django 2.1.1 on 2018-09-24 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flickr', '0020_auto_20180924_1257'),
    ]

    operations = [
        migrations.CreateModel(
            name='FlickrPhotoNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flickr_id', models.CharField(max_length=200)),
                ('photo_id', models.CharField(blank=True, max_length=100, null=True)),
                ('author', models.CharField(blank=True, max_length=200, null=True)),
                ('authorname', models.CharField(blank=True, max_length=200, null=True)),
                ('authorrealname', models.CharField(blank=True, max_length=200, null=True)),
                ('authorispro', models.NullBooleanField()),
                ('authorisdeleted', models.NullBooleanField()),
                ('dimesions', models.TextField(blank=True, null=True)),
                ('content', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
