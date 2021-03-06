# Generated by Django 2.1.1 on 2018-09-23 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flickr', '0005_auto_20180923_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flickrphoto',
            name='comments',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='flickrphoto',
            name='dateuploaded',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='flickrphoto',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='flickrphoto',
            name='farm',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='flickrphoto',
            name='isfavorite',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='flickrphoto',
            name='license',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='flickrphoto',
            name='media',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='flickrphoto',
            name='originalformat',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='flickrphoto',
            name='originalsecret',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='flickrphoto',
            name='rotation',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='flickrphoto',
            name='safety_level',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='flickrphoto',
            name='secret',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='flickrphoto',
            name='server',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='flickrphoto',
            name='title',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='flickrphoto',
            name='views',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='flickrphotodate',
            name='lastupdate',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='flickrphotodate',
            name='posted',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='flickrphotodate',
            name='taken',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='flickrphotodate',
            name='takengranularity',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='flickrphotodate',
            name='takenunknown',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='flickrphotolocation',
            name='accuracy',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='flickrphotolocation',
            name='context',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='flickrphotolocation',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=30, max_digits=50, null=True),
        ),
        migrations.AlterField(
            model_name='flickrphotolocation',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=30, max_digits=50, null=True),
        ),
        migrations.AlterField(
            model_name='flickrphotolocation',
            name='place_id',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='flickrphotolocation',
            name='woeid',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='flickrphotoowner',
            name='iconfarm',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='flickrphotoowner',
            name='iconserver',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='flickrphotoowner',
            name='location',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='flickrphotoowner',
            name='path_alias',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='flickrphotoowner',
            name='realname',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='flickrphotoowner',
            name='username',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='flickrphototag',
            name='author',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='flickrphototag',
            name='authorname',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='flickrphototag',
            name='content',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='flickrphototag',
            name='machine_tag',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='flickrphototag',
            name='raw',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='flickrphotourl',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]
