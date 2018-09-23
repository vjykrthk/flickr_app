from django.db import models
from rest_framework.fields import JSONField


class FlickrGroup(models.Model):
    flckr_id = models.CharField(max_length=200)
    name = models.CharField(max_length=200)


class FlickrPhotos(models.Model):
    flickr_id = models.CharField(max_length=200)
    secret = models.CharField(max_length=200)
    server = models.CharField(max_length=100)
    farm = models.IntegerField()
    dateuploaded = models.DateTimeField()
    isfavorite = models.BooleanField()
    license = models.BooleanField()
    safety_level = models.IntegerField()
    rotation = models.IntegerField()
    originalformat = models.CharField(max_length=50)
    owner = JSONField()
    title = JSONField()
    description = JSONField()
    visibility = JSONField()
    dates = JSONField()
    views = models.IntegerField()
    editability = JSONField()
    publiceditability = JSONField()
    usage = JSONField()
    comments = JSONField()
    notes = JSONField()
    people = JSONField()
    tags = JSONField()
    location = JSONField()
    media = models.CharField(max_length=200)


class FlickrPhotoUrl(models.Model):
    url = models.CharField(max_length=200)
    flickr_photo_id = models.ForeignKey('FlickrPhotos', related_name='urls', on_delete=models.CASCADE)
