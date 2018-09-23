from django.db import models
from rest_framework.fields import JSONField


class FlickrGroup(models.Model):
    flickr_id = models.CharField(max_length=200)
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
    title = models.TextField()
    description = models.TextField()
    ispublic = models.BooleanField(),
    isfriend = models.BooleanField(),
    isfamily = models.BooleanField(),
    views = models.IntegerField()
    editability = JSONField()
    publiceditability = JSONField()
    usage = JSONField()
    comments = models.IntegerField()
    notes = JSONField()
    people = JSONField()
    geoperms = JSONField()
    media = models.CharField(max_length=200)


class FlickrPhotoDates(models.Model):
    posted = models.DateTimeField()
    taken = models.DateTimeField()
    takengranularity = models.IntegerField()
    takenunknown = models.IntegerField()
    lastupdate = models.IntegerField()
    flickr_photo = models.OneToOneField('FlickrPhotos', on_delete=models.CASCADE)


class FlickrOwner(models.Model):
    nsid = models.CharField(max_length=200)
    realname = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    iconserver = models.IntegerField()
    iconfarm = models.IntegerField()
    path_alias = models.CharField(max_length=200)
    flickr_photo = models.ManyToManyField('FlickrPhotos')


class FlickrPhotoTags(models.Model):
    flickr_id = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    authorname = models.CharField(max_length=200)
    raw = models.CharField(max_length=200)
    content = models.CharField(max_length=200)
    machine_tag = models.IntegerField()
    flickr_photo = models.ManyToManyField('FlickrPhotos')


class FlickrPhotoLocation(models.Model):
    latitude = models.DecimalField()
    longitude = models.DecimalField()
    accuracy = models.IntegerField()
    context = models.IntegerField()
    neighbourhood = JSONField()
    locality = JSONField()
    county = JSONField()
    region = JSONField()
    country = JSONField()
    place_id = models.CharField(max_length=200)
    woeid = models.CharField(max_length=200)
    flickr_photo = models.OneToOneField('FlickrPhotos', on_delete=models.CASCADE)


class FlickrPhotoUrls(models.Model):
    url = models.CharField(max_length=200)
    flickr_photo = models.ForeignKey('FlickrPhotos', related_name='urls', on_delete=models.CASCADE)
